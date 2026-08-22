from orchestration.orchestrator import orchestrate

REFERENCE_CONTEXT = {
    "program_goal": "design a coherent curriculum",
    "program_goals_reviewed": True,
    "learning_outcomes_reviewed": True,
    "sequence_reviewed": True,
    "assessment_alignment_reviewed": True,
    "inclusion_accessibility_reviewed": True,
    "evidence_reviewed": True,
    "quality_reviewed": True,
    "human_approval": True,
}

if __name__ == "__main__":
    print(orchestrate(REFERENCE_CONTEXT))
