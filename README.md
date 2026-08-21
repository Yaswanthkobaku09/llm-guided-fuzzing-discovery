# LLM-Guided Fuzzing for Vulnerability Discovery

PhD portfolio project — Tier VI, AI in offensive security. Test whether LLM-guided seed
generation and crash triage actually improves fuzzing over a coverage-guided baseline —
and whether any improvement is genuine generalization or memorized-CTF leakage.

**Authorized-use only.** Target only code you own or are explicitly permitted to fuzz —
this project fuzzes local, intentionally-vulnerable or open-source targets you control,
not third-party production systems.

## The gap

LLM-assisted vulnerability discovery has moved from CTF novelty to real-world impact
fast: an o3-based system found a real authentication zero-day (CVE-2025-37899), Claude
Opus 4.6 identified 22 real vulnerabilities in Firefox, and DARPA's AI Cyber Challenge
awarded $29.5M in prizes across systems that discovered 18 real, previously-unknown bugs
in production software. Critically, AIxCC's designers specifically inserted *fresh* bugs
into the target codebases rather than reusing known CVEs — because standard CTF and CVE
benchmarks are contaminated by public writeups an LLM may have memorized, which inflates
apparent capability. The open methodological problem for anyone building an LLM-guided
fuzzer is the same one AIxCC solved at massive scale: how do you know your system found
the bug, versus recalled it?

## The project

- Wrap a coverage-guided fuzzer (e.g., AFL++) with two LLM-guidance stages: an
  **LLM seed mutator** that proposes structurally-informed input mutations beyond random
  bit-flipping, and an **LLM crash triage agent** that classifies and deduplicates crashes
  by likely root cause
- Build a small **synthetic bug injector** that inserts a handful of fresh, undocumented
  bugs into a target codebase you control
- Run the fuzzer three ways on the same target: baseline (no LLM guidance), LLM-guided,
  and report time-to-first-crash and total unique crashes for both a **memorized set**
  (public CTF-style targets with known bugs) and the **fresh-bug set** — directly
  measuring the memorization-vs-generalization gap AIxCC was designed to expose

## Status

Scaffold stage — fuzzer wrapper, guidance stages, and bug-injection tooling defined,
implementations pending.

## Repository layout

```
src/
  fuzzer/         coverage-guided fuzzer wrapper and seed corpus management
  llm_guidance/   LLM-based seed mutation and crash triage
  targets/        synthetic bug injector for fresh, undocumented test cases
  eval/           time-to-first-crash and memorization-vs-generalization metrics
data/             seed corpora and target binaries (not committed)
```

## Roadmap

1. Get a baseline coverage-guided fuzzer running end-to-end against one public,
   intentionally-vulnerable target
2. Implement the LLM seed mutator; compare coverage growth and crash discovery rate
   against the unguided baseline on the same target
3. Implement the crash triage agent; measure dedup accuracy against manually-labeled
   crashes
4. Build the synthetic bug injector, insert 3-5 fresh bugs into a target you control, and
   re-run the identical pipeline to report the memorized-vs-fresh generalization gap

## Related work

- Fang et al., "LLM Agents can Autonomously Exploit One-day Vulnerabilities" (2024)
- "FuzzingBrain V2: A Multi-Agent LLM System for Automated Vulnerability Discovery and
  Reproduction" (arXiv, 2026)
- "FirmAgent" (NDSS 2026) — LLM + fuzzing for IoT firmware vulnerability discovery
- "D-CIPHER" — multi-agent CTF exploit derivation
- DARPA AI Cyber Challenge (AIxCC) methodology for memorization-controlled evaluation
- "Data-Centric Benchmarking of Exploit Generation in LLMs" (arXiv, 2026)

## License

MIT
