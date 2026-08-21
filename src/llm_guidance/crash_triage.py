"""LLM-based crash triage: classifies and deduplicates raw crashes by
likely root cause (e.g., same underlying bug reached via different inputs).

TODO: implement crash-report summarization and a dedup key derived from
the model's root-cause classification, validated against manually-labeled
crashes.
"""


def triage(crash_report: dict) -> dict:
    raise NotImplementedError


def dedup_key(triaged_crashes: list[dict]) -> list[str]:
    raise NotImplementedError
