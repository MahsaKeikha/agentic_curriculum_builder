# F92 | Agentic Curriculum Builder | L3 Gold Standard | v1.0

A governed multi-agent reference system for curriculum architecture, learning outcomes, sequencing, assessment alignment, inclusion and accessibility, evidence review, and academic quality assurance.

## Five-agent architecture

- Outcome Architect
- Sequence Designer
- Assessment Aligner
- Inclusion Reviewer
- Quality Auditor

## Gold-standard academic governance

F92 is fail closed. Curriculum recommendation release requires reviewed program goals, learning outcomes, sequencing, assessment alignment, inclusion and accessibility, evidence, quality standards, and explicit qualified-human approval.

Release is blocked for outcome-alignment gaps, unresolved prerequisite or sequencing problems, assessment misalignment, accessibility gaps, material inclusion or bias risks, missing evidence provenance, infeasible workload, or unresolved quality and accreditation-standard gaps.

The reference system cannot autonomously approve curricula, change academic policy or program requirements, alter student records, make accreditation claims, or submit externally on behalf of an institution.

## Verification gates

CI runs on Python 3.10, 3.11, and 3.12 and requires:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

The behavioral verification layer includes eight direct governance tests and a 10-scenario held-out curriculum-governance suite.
