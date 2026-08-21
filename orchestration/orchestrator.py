from AGENTS.outcome_architect_agent import run as a
from AGENTS.sequence_designer_agent import run as b
from AGENTS.assessment_aligner_agent import run as c
from AGENTS.inclusion_reviewer_agent import run as d
from AGENTS.quality_auditor_agent import run as e
def orchestrate(context): return [a(context),b(context),c(context),d(context),e(context)]
