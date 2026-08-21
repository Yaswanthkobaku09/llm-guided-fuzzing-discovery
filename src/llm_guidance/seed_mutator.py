"""LLM-guided seed mutator: proposes structurally-informed input mutations
using knowledge of the target's expected input format, rather than random
bit-flipping.

TODO: implement prompt construction from a seed + target format description,
and parsing of the model's proposed mutated input back into bytes.
"""


def propose_mutation(seed: bytes, format_hint: str) -> bytes:
    raise NotImplementedError
