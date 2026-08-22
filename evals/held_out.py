from orchestration.orchestrator import orchestrate


def base():
    return {
        "program_goals_reviewed": True,
        "learning_outcomes_reviewed": True,
        "sequence_reviewed": True,
        "assessment_alignment_reviewed": True,
        "inclusion_accessibility_reviewed": True,
        "evidence_reviewed": True,
        "quality_reviewed": True,
        "human_approval": True,
    }


SCENARIOS = [
    ({}, False),
    (base(), True),
    ({**base(), "human_approval": False}, False),
    ({**base(), "outcome_alignment_gap": True}, False),
    ({**base(), "sequence_prerequisite_gap": True}, False),
    ({**base(), "assessment_misalignment": True}, False),
    ({**base(), "accessibility_gap": True}, False),
    ({**base(), "inclusion_bias_risk": True}, False),
    ({**base(), "evidence_provenance_missing": True}, False),
    ({**base(), "quality_standard_gap": True}, False),
]


def main():
    passed = 0
    for context, expected in SCENARIOS:
        passed += orchestrate(context)["release_allowed"] is expected
    print(f"held-out: {passed}/{len(SCENARIOS)} passed")
    raise SystemExit(0 if passed == len(SCENARIOS) else 1)


if __name__ == "__main__":
    main()
