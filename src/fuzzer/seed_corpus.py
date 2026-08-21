"""Seed corpus management: tracks which seeds came from the baseline
mutator versus the LLM-guided mutator, for later attribution in metrics.

TODO: implement corpus loading, deduplication, and provenance tagging.
"""


def load_corpus(path: str) -> list[bytes]:
    raise NotImplementedError
