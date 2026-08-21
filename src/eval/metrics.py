"""Time-to-first-crash, unique crash count, and the memorized-vs-fresh
generalization gap between the public/memorized target set and the
synthetic fresh-bug set.

TODO: implement metric computation, reported separately per target set
and per fuzzer configuration (baseline / LLM-guided).
"""


def time_to_first_crash(run_log: dict) -> float:
    raise NotImplementedError


def generalization_gap(memorized_set_results: dict, fresh_set_results: dict) -> float:
    raise NotImplementedError
