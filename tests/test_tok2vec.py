import pytest
from numpy.testing import assert_equal
from spacy_pytorch_transformers import PyTT_TokenVectorEncoder
from spacy.vocab import Vocab
import pickle

from .util import make_tempdir, is_valid_tensor


@pytest.fixture
def docs(nlp):
    texts = ["the cat sat on the mat.", "hello world."]
    return [nlp(text) for text in texts]


@pytest.fixture(scope="session")
def tok2vec(name, nlp):
    return nlp.get_pipe("pytt_tok2vec")


def test_from_pretrained(tok2vec, docs):
    docs_out = list(tok2vec.pipe(docs))
    assert len(docs_out) == len(docs)
    for doc in docs_out:
        diff = doc.tensor.sum() - doc._.pytt_last_hidden_state.sum()
        assert abs(diff) <= 1e-2


@pytest.mark.parametrize(
    "text1,text2,is_similar,threshold",
    [
        ("The dog barked.", "The puppy barked.", True, 0.5),
        ("rats are cute", "cats please me", True, 0.6),
    ],
)
def test_similarity(nlp, text1, text2, is_similar, threshold):
    doc1 = nlp(text1)
    doc2 = nlp(text2)
    similarity = doc1.similarity(doc2)
    if is_similar:
        assert similarity >= threshold
    else:
        assert similarity < threshold


def test_tok2vec_to_from_bytes(tok2vec, docs):
    doc = tok2vec(docs[0])
    assert is_valid_tensor(doc.tensor)
    bytes_data = tok2vec.to_bytes()
    new_tok2vec = PyTT_TokenVectorEncoder(Vocab(), **tok2vec.cfg)
    with pytest.raises(ValueError):
        new_doc = new_tok2vec(docs[0])
    new_tok2vec.from_bytes(bytes_data)
    new_doc = new_tok2vec(docs[0])
    assert is_valid_tensor(new_doc.tensor)
    assert_equal(doc.tensor, new_doc.tensor)


def test_tok2vec_to_from_disk(tok2vec, docs):
    doc = tok2vec(docs[0])
    assert is_valid_tensor(doc.tensor)
    with make_tempdir() as tempdir:
        file_path = tempdir / "tok2vec"
        tok2vec.to_disk(file_path)
        new_tok2vec = PyTT_TokenVectorEncoder(Vocab())
        new_tok2vec.from_disk(file_path)
    new_doc = new_tok2vec(docs[0])
    assert is_valid_tensor(new_doc.tensor)
    assert_equal(doc.tensor, new_doc.tensor)


# Fails on 3.6 due to type annotations :(. See
# https://github.com/cloudpipe/cloudpickle/pull/299
@pytest.mark.xfail
def test_tok2vec_pickle_dumps_loads(tok2vec, docs):
    doc = tok2vec(docs[0])
    assert is_valid_tensor(doc.tensor)
    pkl_data = pickle.dumps(tok2vec)
    new_tok2vec = pickle.loads(pkl_data)
    new_doc = new_tok2vec(docs[0])
    assert is_valid_tensor(new_doc.tensor)
    assert_equal(doc.tensor, new_doc.tensor)
