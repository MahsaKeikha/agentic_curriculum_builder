from AGENTS.assessment_aligner_agent import run as assessment
from AGENTS.inclusion_reviewer_agent import run as inclusion
from AGENTS.outcome_architect_agent import run as outcomes
from AGENTS.quality_auditor_agent import run as quality
from AGENTS.sequence_designer_agent import run as sequence
from safety.policy import authorize


def orchestrate(context: dict) -> dict:
    """Run curriculum specialists and apply fail-closed academic governance."""
    results = [
        outcomes(context),
        sequence(context),
        assessment(context),
        inclusion(context),
        quality(context),
    ]
    governance = authorize("curriculum_recommendation_release", context)
    return {
        "system": "F92",
        "results": results,
        "governance": governance,
        "release_allowed": governance["allowed"],
        "human_review_required": True,
        "autonomous_curriculum_authority": False,
    }
