"""Fail-closed governance for F92 curriculum design."""

PROTECTED_ACTIONS = {
    "curriculum_approval",
    "policy_change",
    "student_record_change",
    "external_submission",
    "program_requirement_change",
    "accreditation_claim",
}

REQUIRED_REVIEWS = (
    "program_goals_reviewed",
    "learning_outcomes_reviewed",
    "sequence_reviewed",
    "assessment_alignment_reviewed",
    "inclusion_accessibility_reviewed",
    "evidence_reviewed",
    "quality_reviewed",
    "human_approval",
)


def authorize(action: str, context: dict | None = None) -> dict:
    context = context or {}
    if action in PROTECTED_ACTIONS:
        return {"allowed": False, "reason": "binding academic authority is outside reference-system scope"}

    missing = [key for key in REQUIRED_REVIEWS if not context.get(key)]
    if missing:
        return {"allowed": False, "reason": "missing required curriculum review", "missing": missing}

    blockers = []
    if context.get("outcome_alignment_gap"):
        blockers.append("learning outcomes are not adequately aligned")
    if context.get("sequence_prerequisite_gap"):
        blockers.append("prerequisite or sequencing gap unresolved")
    if context.get("assessment_misalignment"):
        blockers.append("assessment does not validly measure stated outcomes")
    if context.get("accessibility_gap"):
        blockers.append("accessibility requirement unresolved")
    if context.get("inclusion_bias_risk"):
        blockers.append("material inclusion or bias risk unresolved")
    if context.get("evidence_provenance_missing"):
        blockers.append("curriculum evidence provenance incomplete")
    if context.get("workload_infeasible"):
        blockers.append("learner or instructional workload is infeasible")
    if context.get("quality_standard_gap"):
        blockers.append("quality or accreditation standard gap unresolved")

    if blockers:
        return {"allowed": False, "reason": "curriculum governance blocker", "blockers": blockers}

    return {"allowed": True, "reason": "curriculum package approved for recommendation after qualified human review"}


def review_required(action: str) -> bool:
    return action in PROTECTED_ACTIONS


def enforce(action: str, approved: bool) -> None:
    if review_required(action) and not approved:
        raise PermissionError("Qualified human approval is required for this action.")
