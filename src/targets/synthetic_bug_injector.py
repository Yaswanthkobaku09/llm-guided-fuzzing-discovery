"""Inserts a small number of fresh, undocumented bugs into a target
codebase you control, so fuzzer performance can be measured on cases with
zero chance of being memorized from public sources.

TODO: implement controlled bug injection (e.g., off-by-one, missing bounds
check) with a manifest recording exactly what was injected and where, for
later ground-truth comparison.
"""


def inject_bugs(source_path: str, bug_count: int) -> dict:
    """Returns a manifest of injected bugs for ground-truth comparison."""
    raise NotImplementedError
