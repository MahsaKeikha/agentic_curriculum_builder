# F92 Agentic Curriculum Builder

**Maturity:** L3 Gold Standard  
**Version:** 1.0.0

A governed five-agent reference architecture for curriculum design across program outcomes, sequencing, prerequisite structure, assessment alignment, inclusion and accessibility, gap analysis, quality assurance, and qualified academic approval.

F92 is intended as a reusable multi-agent framework for departments, programs, curriculum committees, academic leaders, and faculty teams that need a traceable way to design or review curricula without transferring institutional authority to an automated system.

This repository supports curriculum planning and review. It does not autonomously approve curricula, modify degree requirements, change academic policy, make accreditation claims, alter student records, or submit externally on behalf of an institution.

## Curriculum lifecycle

```text
program goals + constraints
          |
          v
   outcome architecture
          |
          v
   curriculum sequencing
          |
          v
 assessment alignment
          |
          v
 inclusion + accessibility
          |
          v
     quality audit
          |
          v
 qualified academic approval
```

The workflow is fail closed. Outcome gaps, prerequisite problems, sequencing conflicts, assessment misalignment, inaccessible requirements, infeasible workload, unsupported accreditation mappings, missing evidence, or unresolved quality issues remain blockers.

## Five-agent architecture

| Agent | Responsibility | Core question |
|---|---|---|
| Outcome Architect Agent | Defines program outcomes, competencies, and measurable learning expectations | What should graduates know, be able to do, and demonstrate by program completion? |
| Sequence Designer Agent | Structures prerequisite dependencies, course progression, and developmental sequencing | Are students given the required foundation before advanced learning is expected? |
| Assessment Aligner Agent | Maps outcomes and competencies to assessment evidence | Where and how is each program outcome actually assessed? |
| Inclusion Reviewer Agent | Reviews accessibility, inclusion, participation barriers, and equity implications | Does the curriculum create avoidable barriers without academic justification? |
| Quality Auditor Agent | Reviews coherence, completeness, evidence, standards mapping, and release readiness | Is the curriculum internally consistent, auditable, and ready for qualified human approval? |

The agents provide structured recommendations. They do not independently exercise curriculum committee, faculty senate, registrar, accreditation, or institutional authority.

## Repository structure

```text
AGENTS/
├── outcome_architect_agent.py
├── sequence_designer_agent.py
├── assessment_aligner_agent.py
├── inclusion_reviewer_agent.py
└── quality_auditor_agent.py

SKILLS/
├── outcome_design.py
├── curriculum_sequencing.py
├── assessment_alignment.py
├── inclusive_design.py
└── curriculum_audit.py

TOOLS/
├── outcome_map_tool.py
├── prerequisite_graph_tool.py
├── assessment_matrix_tool.py
├── accessibility_check_tool.py
└── gap_analysis_tool.py

orchestration/
memory/
state/
schemas/
prompts/
config/
safety/
observability/
evals/
benchmarks/
examples/
tests/
docs/
.github/workflows/ci.yml
run.py
pyproject.toml
README.md
```

The structure separates curriculum reasoning from deterministic maps, dependency graphs, alignment matrices, governance checks, evaluation, and observability.

## Program context

A useful program record can include:

```text
program_id
program_name
degree_level
credit_requirement
program_length
student_population
entry_requirements
program_goals
program_outcomes
required_courses
electives
prerequisites
capstone_requirements
laboratory_requirements
clinical_or_field_requirements
accreditation_context
institutional_policies
faculty_owner
```

Curriculum recommendations should be interpreted within the actual discipline, institution, jurisdiction, delivery model, and student population.

## Program goals and learning outcomes

Program goals describe broad educational purpose. Program learning outcomes describe observable expectations of graduate performance.

Outcomes may address:

- disciplinary knowledge
- analysis
- design
- experimentation
- research
- communication
- teamwork
- ethics
- professional judgment
- data literacy
- computation
- leadership
- lifelong learning

Outcomes should be specific enough to map to course-level learning and actual assessment evidence.

## Outcome architecture

The Outcome Architect Agent structures the relationship among institutional goals, program goals, program outcomes, course outcomes, competencies, and assessment evidence.

```text
institutional mission
        |
        v
program goals
        |
        v
program outcomes
        |
        v
course outcomes
        |
        v
learning activities + assessments
```

`TOOLS/outcome_map_tool.py` provides deterministic support for this mapping.

## Competency models

Programs that use competency-based structures can record:

```text
competency_id
competency_name
description
expected_level
where_introduced
where_reinforced
where_mastered
assessment_evidence
```

F92 does not assume one competency taxonomy fits every discipline.

## Introduce, reinforce, master

Curriculum mapping can use developmental levels such as:

```text
I = Introduced
R = Reinforced
M = Mastered
```

The labels can vary. The important point is to make progression visible.

A required program outcome should not appear only at the end of the curriculum unless that design is intentional and academically justified.

## Curriculum sequencing

The Sequence Designer Agent examines whether learning dependencies are respected.

Sequence review can include:

- prerequisite knowledge
- co-requisites
- mathematical progression
- laboratory dependencies
- theory before application
- design progression
- research progression
- communication development
- internship or field preparation
- capstone readiness

Sequencing should support development rather than merely preserve historical course numbering.

## Prerequisite graph

`TOOLS/prerequisite_graph_tool.py` supports deterministic course dependency mapping.

It can help expose:

- circular prerequisites
- missing prerequisites
- impossible pathways
- unnecessary bottlenecks
- hidden dependencies
- excessive prerequisite chains
- single points of failure in progression

Prerequisite requirements should be based on actual learning dependencies whenever possible.

## Horizontal alignment

Horizontal alignment reviews courses taken at the same stage.

Questions include:

- Are concurrent courses using compatible prerequisite assumptions?
- Are major deadlines clustered unnecessarily?
- Are related concepts being taught in disconnected ways?
- Are laboratories aligned with related theory courses?
- Are students asked to use tools or methods before learning them elsewhere in the term?

## Vertical alignment

Vertical alignment reviews development across stages or years.

Questions include:

- Is introductory knowledge built upon later?
- Are advanced courses requiring skills that were never reinforced?
- Is content repeated without increasing complexity?
- Does the capstone rely on competencies that were developed earlier?

A coherent curriculum should show intentional progression rather than disconnected repetition.

## Course-to-program mapping

Each course can be mapped to one or more program outcomes.

A useful map can include:

```text
course_id
program_outcome
coverage_level
instructional_emphasis
assessment_evidence
required_or_elective
```

Coverage should not automatically be treated as evidence of attainment.

## Assessment alignment

The Assessment Aligner Agent reviews whether outcomes are actually measured.

`TOOLS/assessment_matrix_tool.py` supports structured mapping of outcomes to assessment evidence.

Evidence can include:

- examinations
- laboratories
- design projects
- portfolios
- presentations
- research projects
- capstones
- clinical demonstrations
- field evaluations
- standardized assessments

The assessment format should match the nature of the outcome.

## Direct and indirect evidence

Programs often use both direct and indirect evidence.

**Direct evidence** evaluates student work or demonstrated performance.

**Indirect evidence** can include surveys, self-assessment, alumni feedback, employer feedback, or perception measures.

Indirect evidence can be useful, but it should not silently substitute for direct demonstration when direct evidence is required.

## Assessment coverage gaps

The alignment matrix can expose outcomes that are:

- not assessed
- assessed only once
- assessed only indirectly
- assessed only in electives
- assessed without clear criteria
- assessed at the wrong developmental level

These gaps remain visible until they are resolved or intentionally accepted by qualified faculty.

## Gap analysis

`TOOLS/gap_analysis_tool.py` supports structured identification of weak or missing curriculum coverage.

Gap analysis can examine:

- outcomes with no course coverage
- courses with no clear program contribution
- prerequisite gaps
- missing advanced development
- assessment gaps
- accessibility gaps
- workload gaps
- standards-mapping gaps

Not every gap requires a new course. Some are better addressed through redesign, integration, sequencing, or assessment changes.

## Reinforcement versus redundancy

Repeated content can be appropriate when complexity increases. It becomes inefficient when students repeat essentially identical material without deeper application.

The workflow should distinguish intentional reinforcement from unnecessary duplication.

## Breadth and depth

Programs often balance foundational breadth with disciplinary depth and specialization.

Review can include:

- foundational coverage
- major-specific depth
- technical electives
- general education
- interdisciplinary learning
- professional skills
- research opportunities
- emerging topics

F92 does not prescribe one universal balance.

## Credit and workload analysis

Curriculum feasibility depends on more than total credit count.

Review can consider:

- contact hours
- independent work
- laboratory load
- project load
- reading load
- assessment concentration
- capstone demands
- clinical or field hours
- concurrent course intensity

A program can satisfy credit limits while still creating unreasonable workload peaks.

## Bottleneck courses

Some courses strongly affect progression.

A bottleneck review can consider:

- limited offering frequency
- prerequisite position
- scheduling conflicts
- laboratory capacity
- instructor availability
- transfer equivalencies
- historically high repeat demand

F92 can identify structural risk but does not determine academic standards or grading policy.

## Elective architecture

Elective design can support specialization while preserving program coherence.

Review can consider:

- elective categories
- minimum depth requirements
- prerequisites
- scheduling availability
- capacity
- outcome coverage
- overlap among electives

A program should not rely on a single elective for required outcome evidence unless every student has an equivalent guaranteed pathway.

## Capstone alignment

A capstone can provide integrative evidence across multiple outcomes.

Review can examine whether students enter the capstone with sufficient preparation in:

- domain knowledge
- design or analysis
- communication
- teamwork
- research methods
- ethics
- project planning
- discipline-specific tools

A capstone should integrate prior learning rather than compensate for major curriculum gaps that were never addressed earlier.

## Inclusion and accessibility

The Inclusion Reviewer Agent examines whether curriculum structure creates avoidable barriers.

`TOOLS/accessibility_check_tool.py` can support checks related to:

- digital accessibility
- laboratory accessibility
- physical access
- alternative formats
- captioning and transcripts
- accessible equations and tables
- scheduling barriers
- prerequisite assumptions
- required technologies
- field or travel requirements

Accessibility should be considered at the program design level rather than only after individual barriers arise.

## Inclusion and academic standards

Inclusive design does not require removing legitimate academic requirements.

The workflow should distinguish between:

```text
essential academic requirement
and
avoidable implementation barrier
```

That distinction remains a qualified academic judgment.

## Bias and representation

Curriculum review can consider whether examples, case studies, authors, datasets, historical perspectives, or professional contexts are unnecessarily narrow for the discipline.

The goal is not to impose one representation model. It is to surface material omissions, stereotypes, or barriers that may affect learning or professional preparation.

## Accreditation and external standards

Programs may map curricula to accreditation criteria, professional standards, licensure expectations, or institutional frameworks.

A standards mapping should preserve:

```text
standard_id
standard_source
standard_version
program_outcome
course_evidence
assessment_evidence
responsible_owner
review_state
```

F92 can organize this evidence but does not independently claim accreditation compliance or approval.

## Evidence provenance

Curriculum decisions may rely on:

- institutional policy
- accreditation standards
- professional standards
- disciplinary guidance
- labor-market analysis
- educational research
- advisory-board input
- faculty judgment
- student feedback
- alumni feedback

Material evidence should retain source, version, applicability, and limitations.

## Curriculum audit

`SKILLS/curriculum_audit.py` supports systematic quality review of the whole curriculum.

The Quality Auditor Agent can review:

- outcome completeness
- sequencing coherence
- prerequisite integrity
- assessment alignment
- workload
- accessibility
- inclusion
- standards mapping
- evidence quality
- unresolved gaps

This independent review path helps avoid having the same reasoning process both design and approve the curriculum.

## Curriculum versioning

Curricula evolve over time.

Versioning should preserve:

- prior requirements
- new requirements
- transition rules
- course substitutions
- deleted courses
- added courses
- changed prerequisites
- changed outcome mappings
- changed assessment mappings
- effective term
- student catalog rights where applicable

A revised curriculum should not silently overwrite the record of the version under which existing students entered.

## Change impact analysis

Before a curriculum change is adopted, review can identify impacts on:

- current students
- incoming students
- prerequisite chains
- course scheduling
- faculty load
- laboratory capacity
- accreditation evidence
- transfer articulation
- graduation timelines

A small course change can have large downstream effects when it sits early in a dependency chain.

## Transition planning

Curriculum changes often require teach-out or transition plans.

A transition record can identify:

- affected cohorts
- equivalent courses
- substitutions
- expiration dates
- advising implications
- scheduling implications
- approval owners

F92 can structure transition analysis but does not modify student records.

## Student data boundary

Curriculum design usually does not require detailed identifiable student data.

Where student outcomes or progression data are used, implementations should minimize exposure and follow applicable institutional privacy requirements.

The system should not make unsupported judgments about individual students from aggregate curriculum data.

## Observability

The `observability/` layer supports traceability of the multi-agent workflow.

Useful curriculum telemetry includes:

- outcome mappings
- prerequisite conflicts
- assessment gaps
- accessibility findings
- workload flags
- standards-mapping gaps
- change-impact findings
- unresolved quality issues
- human-review state

Observability supports auditability. It does not create academic authority.

## Fail-closed governance

Curriculum recommendation release is blocked when material issues remain unresolved.

Reference blockers include:

- program goals incomplete
- program outcomes incomplete
- outcome mapping gap
- prerequisite cycle
- prerequisite gap
- sequencing conflict
- assessment alignment failure
- required outcome assessed only indirectly
- inaccessible curriculum requirement
- infeasible workload
- unresolved inclusion concern
- standards mapping unsupported
- evidence provenance missing
- change impact unreviewed
- curriculum approval requested without authorized human process
- qualified human approval missing

The system should surface the blocker rather than manufacture a complete-looking curriculum.

## Human authority boundaries

F92 must not autonomously:

- approve a curriculum
- create or eliminate degree requirements
- change academic policy
- change catalog rules
- modify student records
- waive prerequisites for individual students
- determine transfer credit
- determine graduation eligibility
- make accreditation claims
- submit externally on behalf of an institution
- fabricate standards mappings or academic evidence

Final authority remains with qualified faculty and authorized institutional governance bodies.

## End-to-end reference workflow

A typical F92 workflow follows this sequence:

1. Define program goals, constraints, and academic context.
2. Define measurable program outcomes or competencies.
3. Map outcomes to required and elective courses.
4. Build the prerequisite graph.
5. Review horizontal and vertical sequencing.
6. Identify coverage gaps and unnecessary redundancy.
7. Map program outcomes to direct and indirect assessment evidence.
8. Review credit load, workload, bottlenecks, and scheduling feasibility.
9. Review accessibility and inclusion.
10. Map relevant external standards with versioned provenance.
11. Review capstone and integrative learning alignment.
12. Perform curriculum gap and quality audits.
13. Analyze impacts of proposed changes and transition requirements.
14. Apply fail-closed governance gates.
15. Require qualified academic approval before institutional adoption.

## Evaluation and held-out governance suite

The repository includes evaluation logic under `evals/` and benchmark material under `benchmarks/`.

Evaluation should test both curriculum quality and governance behavior.

Useful dimensions include:

- outcome completeness
- outcome-map consistency
- prerequisite integrity
- sequencing quality
- assessment alignment
- accessibility enforcement
- gap detection
- workload detection
- standards-provenance enforcement
- change-impact awareness
- academic-authority boundaries
- human-approval enforcement

The held-out suite should include intentionally flawed curricula that appear plausible but contain hidden prerequisite, alignment, accessibility, or governance failures.

## Failure states

Useful explicit states include:

```text
PROGRAM GOALS INCOMPLETE
PROGRAM OUTCOMES INCOMPLETE
OUTCOME MAPPING GAP
PREREQUISITE CYCLE
PREREQUISITE GAP
SEQUENCING CONFLICT
ASSESSMENT ALIGNMENT FAILURE
DIRECT EVIDENCE GAP
ACCESSIBILITY GAP
WORKLOAD INFEASIBLE
INCLUSION REVIEW REQUIRED
STANDARDS MAPPING UNSUPPORTED
EVIDENCE PROVENANCE MISSING
CHANGE IMPACT UNREVIEWED
CURRICULUM APPROVAL AUTHORITY PROHIBITED
HUMAN APPROVAL REQUIRED
```

The system should never fabricate outcome attainment, accreditation evidence, student eligibility, institutional approval, or human review.

## Reproduce the reference implementation

Install development dependencies:

```bash
python -m pip install -e '.[dev]'
```

Run the repository checks:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python examples/example.py
python run.py
```

CI under `.github/workflows/ci.yml` validates Python 3.10, 3.11, and 3.12.

## Reproducibility

For a curriculum review intended to be reproducible, version at minimum:

- program goals
- program outcomes
- curriculum map
- prerequisite graph
- assessment matrix
- standards mappings
- accessibility review
- workload assumptions
- course inventory
- effective term
- change history
- evaluation results
- unresolved issues
- approval state

Material revisions should generate a new curriculum version rather than silently replacing the prior record.

## L3 Gold Standard

F92 follows the library's L3 Gold Standard structure through five specialist agents, deterministic curriculum tools, explicit orchestration and state, safety boundaries, observability, held-out governance evaluation, CI, fail-closed release gates, and mandatory qualified academic review.

This maturity designation describes the repository's engineering and governance structure. It is not curriculum approval, institutional accreditation, legal compliance, degree authorization, or permission to modify student records.

## Extending F92

Common extensions include:

- curriculum-management systems
- learning-management systems
- degree-audit systems
- course catalogs
- accreditation evidence systems
- institutional policy repositories
- assessment platforms
- workload models
- advising systems
- student-success analytics
- labor-market data
- prerequisite analytics

New integrations should preserve privacy, evidence provenance, curriculum versioning, institutional policy, access control, and qualified human authority.

## Example applications

F92 can serve as a reference architecture for:

- undergraduate programs
- graduate programs
- engineering curricula
- health-science programs
- professional programs
- certificate programs
- interdisciplinary programs
- curriculum redesign
- accreditation preparation
- program outcome mapping
- prerequisite review
- assessment alignment
- curriculum modernization

Each implementation should be adapted to the discipline, institution, students, professional requirements, and applicable standards.

## Design principles

1. Start with explicit program goals and measurable outcomes.
2. Map learning progression rather than treating courses as isolated units.
3. Make prerequisite dependencies visible and testable.
4. Distinguish course coverage from actual assessment evidence.
5. Use direct evidence where direct demonstration is required.
6. Design accessibility and inclusion into the curriculum structure.
7. Review workload and bottlenecks at the program level.
8. Preserve standards, evidence, and curriculum-version provenance.
9. Analyze change impacts before adopting revisions.
10. Keep final curriculum and institutional authority with qualified humans.

## Documentation

Additional architecture documentation is available under `docs/`, including `docs/ARCHITECTURE.md`.

## Citation and reuse

Use the repository metadata and citation information supplied by the project when referencing this implementation. The repository can be studied, cited, adapted, and extended subject to its license terms.

## Responsible use

Use F92 as a curriculum-design and academic-governance reference architecture. Validate outcomes, sequencing, prerequisites, assessment evidence, accessibility, workload, standards mappings, and institutional requirements against the actual academic program before relying on results. Final curriculum decisions remain with appropriately qualified and authorized humans.