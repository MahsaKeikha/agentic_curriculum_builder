from orchestration.orchestrator import orchestrate
from safety.policy import authorize


def valid_context():
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


def test_complete_review_can_release_recommendation():
    result = orchestrate(valid_context())
    assert result["release_allowed"] is True
    assert result["autonomous_curriculum_authority"] is False


def test_missing_human_approval_fails_closed():
    context = valid_context()
    context["human_approval"] = False
    assert orchestrate(context)["release_allowed"] is False


def test_curriculum_approval_is_never_autonomous():
    assert authorize("curriculum_approval", valid_context())["allowed"] is False


def test_outcome_alignment_gap_blocks_release():
    context = valid_context()
    context["outcome_alignment_gap"] = True
    assert orchestrate(context)["release_allowed"] is False


def test_assessment_misalignment_blocks_release():
    context = valid_context()
    context["assessment_misalignment"] = True
    assert orchestrate(context)["release_allowed"] is False


def test_accessibility_gap_blocks_release():
    context = valid_context()
    context["accessibility_gap"] = True
    assert orchestrate(context)["release_allowed"] is False


def test_evidence_provenance_gap_blocks_release():
    context = valid_context()
    context["evidence_provenance_missing"] = True
    assert orchestrate(context)["release_allowed"] is False


def test_quality_standard_gap_blocks_release():
    context = valid_context()
    context["quality_standard_gap"] = True
    assert orchestrate(context)["release_allowed"] is False
