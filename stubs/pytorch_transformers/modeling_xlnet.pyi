# Stubs for pytorch_transformers.modeling_xlnet (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .modeling_utils import CONFIG_NAME, PoolerAnswerClass, PoolerEndLogits, PoolerStartLogits, PreTrainedModel, PretrainedConfig, SequenceSummary, WEIGHTS_NAME, add_start_docstrings
from torch import nn
from typing import Any, Optional

logger: Any
XLNET_PRETRAINED_MODEL_ARCHIVE_MAP: Any
XLNET_PRETRAINED_CONFIG_ARCHIVE_MAP: Any

def build_tf_xlnet_to_pytorch_map(model: Any, config: Any, tf_weights: Optional[Any] = ...): ...
def load_tf_weights_in_xlnet(model: Any, config: Any, tf_path: Any): ...
def gelu(x: Any): ...
def swish(x: Any): ...

ACT2FN: Any

class XLNetConfig(PretrainedConfig):
    pretrained_config_archive_map: Any = ...
    n_token: Any = ...
    d_model: Any = ...
    n_layer: Any = ...
    n_head: Any = ...
    d_head: Any = ...
    ff_activation: Any = ...
    d_inner: Any = ...
    untie_r: Any = ...
    attn_type: Any = ...
    initializer_range: Any = ...
    layer_norm_eps: Any = ...
    dropout: Any = ...
    mem_len: Any = ...
    reuse_len: Any = ...
    bi_data: Any = ...
    clamp_len: Any = ...
    same_length: Any = ...
    finetuning_task: Any = ...
    num_labels: Any = ...
    summary_type: Any = ...
    summary_use_proj: Any = ...
    summary_activation: Any = ...
    summary_last_dropout: Any = ...
    start_n_top: Any = ...
    end_n_top: Any = ...
    def __init__(self, vocab_size_or_config_json_file: int = ..., d_model: int = ..., n_layer: int = ..., n_head: int = ..., d_inner: int = ..., ff_activation: str = ..., untie_r: bool = ..., attn_type: str = ..., initializer_range: float = ..., layer_norm_eps: float = ..., dropout: float = ..., mem_len: Optional[Any] = ..., reuse_len: Optional[Any] = ..., bi_data: bool = ..., clamp_len: int = ..., same_length: bool = ..., finetuning_task: Optional[Any] = ..., num_labels: int = ..., summary_type: str = ..., summary_use_proj: bool = ..., summary_activation: str = ..., summary_last_dropout: float = ..., start_n_top: int = ..., end_n_top: int = ..., **kwargs: Any) -> None: ...
    @property
    def max_position_embeddings(self): ...
    @property
    def vocab_size(self): ...
    @vocab_size.setter
    def vocab_size(self, value: Any) -> None: ...
    @property
    def hidden_size(self): ...
    @property
    def num_attention_heads(self): ...
    @property
    def num_hidden_layers(self): ...

class XLNetLayerNorm(nn.Module):
    weight: Any = ...
    bias: Any = ...
    variance_epsilon: Any = ...
    def __init__(self, d_model: Any, eps: float = ...) -> None: ...
    def forward(self, x: Any): ...

class XLNetRelativeAttention(nn.Module):
    output_attentions: Any = ...
    n_head: Any = ...
    d_head: Any = ...
    d_model: Any = ...
    scale: Any = ...
    q: Any = ...
    k: Any = ...
    v: Any = ...
    o: Any = ...
    r: Any = ...
    r_r_bias: Any = ...
    r_s_bias: Any = ...
    r_w_bias: Any = ...
    seg_embed: Any = ...
    layer_norm: Any = ...
    dropout: Any = ...
    def __init__(self, config: Any) -> None: ...
    def prune_heads(self, heads: Any) -> None: ...
    @staticmethod
    def rel_shift(x: Any, klen: int = ...): ...
    def rel_attn_core(self, q_head: Any, k_head_h: Any, v_head_h: Any, k_head_r: Any, seg_mat: Optional[Any] = ..., attn_mask: Optional[Any] = ..., head_mask: Optional[Any] = ...): ...
    def post_attention(self, h: Any, attn_vec: Any, residual: bool = ...): ...
    def forward(self, h: Any, g: Any, attn_mask_h: Any, attn_mask_g: Any, r: Any, seg_mat: Any, mems: Optional[Any] = ..., target_mapping: Optional[Any] = ..., head_mask: Optional[Any] = ...): ...

class XLNetFeedForward(nn.Module):
    layer_norm: Any = ...
    layer_1: Any = ...
    layer_2: Any = ...
    dropout: Any = ...
    activation_function: Any = ...
    def __init__(self, config: Any) -> None: ...
    def forward(self, inp: Any): ...

class XLNetLayer(nn.Module):
    rel_attn: Any = ...
    ff: Any = ...
    dropout: Any = ...
    def __init__(self, config: Any) -> None: ...
    def forward(self, output_h: Any, output_g: Any, attn_mask_h: Any, attn_mask_g: Any, r: Any, seg_mat: Any, mems: Optional[Any] = ..., target_mapping: Optional[Any] = ..., head_mask: Optional[Any] = ...): ...

class XLNetPreTrainedModel(PreTrainedModel):
    config_class: Any = ...
    pretrained_model_archive_map: Any = ...
    load_tf_weights: Any = ...
    base_model_prefix: str = ...
    def __init__(self, *inputs: Any, **kwargs: Any) -> None: ...
    def init_weights(self, module: Any) -> None: ...

XLNET_START_DOCSTRING: str
XLNET_INPUTS_DOCSTRING: str

class XLNetModel(XLNetPreTrainedModel):
    output_attentions: Any = ...
    output_hidden_states: Any = ...
    mem_len: Any = ...
    reuse_len: Any = ...
    d_model: Any = ...
    same_length: Any = ...
    attn_type: Any = ...
    bi_data: Any = ...
    clamp_len: Any = ...
    n_layer: Any = ...
    word_embedding: Any = ...
    mask_emb: Any = ...
    layer: Any = ...
    dropout: Any = ...
    def __init__(self, config: Any) -> None: ...
    def create_mask(self, qlen: Any, mlen: Any): ...
    def cache_mem(self, curr_out: Any, prev_mem: Any): ...
    @staticmethod
    def positional_embedding(pos_seq: Any, inv_freq: Any, bsz: Optional[Any] = ...): ...
    def relative_positional_encoding(self, qlen: Any, klen: Any, bsz: Optional[Any] = ...): ...
    def forward(self, input_ids: Any, token_type_ids: Optional[Any] = ..., input_mask: Optional[Any] = ..., attention_mask: Optional[Any] = ..., mems: Optional[Any] = ..., perm_mask: Optional[Any] = ..., target_mapping: Optional[Any] = ..., head_mask: Optional[Any] = ...): ...

class XLNetLMHeadModel(XLNetPreTrainedModel):
    attn_type: Any = ...
    same_length: Any = ...
    transformer: Any = ...
    lm_loss: Any = ...
    def __init__(self, config: Any) -> None: ...
    def tie_weights(self) -> None: ...
    def forward(self, input_ids: Any, token_type_ids: Optional[Any] = ..., input_mask: Optional[Any] = ..., attention_mask: Optional[Any] = ..., mems: Optional[Any] = ..., perm_mask: Optional[Any] = ..., target_mapping: Optional[Any] = ..., labels: Optional[Any] = ..., head_mask: Optional[Any] = ...): ...

class XLNetForSequenceClassification(XLNetPreTrainedModel):
    num_labels: Any = ...
    transformer: Any = ...
    sequence_summary: Any = ...
    logits_proj: Any = ...
    def __init__(self, config: Any) -> None: ...
    def forward(self, input_ids: Any, token_type_ids: Optional[Any] = ..., input_mask: Optional[Any] = ..., attention_mask: Optional[Any] = ..., mems: Optional[Any] = ..., perm_mask: Optional[Any] = ..., target_mapping: Optional[Any] = ..., labels: Optional[Any] = ..., head_mask: Optional[Any] = ...): ...

class XLNetForQuestionAnswering(XLNetPreTrainedModel):
    start_n_top: Any = ...
    end_n_top: Any = ...
    transformer: Any = ...
    start_logits: Any = ...
    end_logits: Any = ...
    answer_class: Any = ...
    def __init__(self, config: Any) -> None: ...
    def forward(self, input_ids: Any, token_type_ids: Optional[Any] = ..., input_mask: Optional[Any] = ..., attention_mask: Optional[Any] = ..., mems: Optional[Any] = ..., perm_mask: Optional[Any] = ..., target_mapping: Optional[Any] = ..., start_positions: Optional[Any] = ..., end_positions: Optional[Any] = ..., cls_index: Optional[Any] = ..., is_impossible: Optional[Any] = ..., p_mask: Optional[Any] = ..., head_mask: Optional[Any] = ...): ...
