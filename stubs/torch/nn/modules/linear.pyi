# Stubs for torch.nn.modules.linear (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from ..._jit_internal import weak_module, weak_script_method
from .module import Module
from typing import Any

class Identity(Module):
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def forward(self, input: Any): ...

class Linear(Module):
    __constants__: Any = ...
    in_features: Any = ...
    out_features: Any = ...
    weight: Any = ...
    bias: Any = ...
    def __init__(self, in_features: Any, out_features: Any, bias: bool = ...) -> None: ...
    def reset_parameters(self) -> None: ...
    def forward(self, input: Any): ...
    def extra_repr(self): ...

class Bilinear(Module):
    __constants__: Any = ...
    in1_features: Any = ...
    in2_features: Any = ...
    out_features: Any = ...
    weight: Any = ...
    bias: Any = ...
    def __init__(self, in1_features: Any, in2_features: Any, out_features: Any, bias: bool = ...) -> None: ...
    def reset_parameters(self) -> None: ...
    def forward(self, input1: Any, input2: Any): ...
    def extra_repr(self): ...
