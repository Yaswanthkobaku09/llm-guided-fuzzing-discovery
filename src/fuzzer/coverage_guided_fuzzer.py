"""Thin wrapper around a coverage-guided fuzzer (e.g., AFL++) exposing a
Python interface for seed injection and crash collection.

TODO: implement subprocess management around the underlying fuzzer binary
and structured crash/coverage reporting back to the pipeline.
"""


class CoverageGuidedFuzzer:
    def __init__(self, target_binary: str, seed_dir: str):
        self.target_binary = target_binary
        self.seed_dir = seed_dir

    def run(self, duration_s: int) -> dict:
        raise NotImplementedError
