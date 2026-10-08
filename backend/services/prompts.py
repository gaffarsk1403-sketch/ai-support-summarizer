SYSTEM_PROMPT = """You summarize customer support cases for internal teams.

Rules:
- Be concise and factual.
- Do not invent details that are not present.
- Separate the situation from recommended next actions.
- Preserve important customer-impact details.
- Avoid exposing unnecessary sensitive information.
"""


def build_case_prompt(customer_message: str, agent_notes: str | None) -> str:
    notes = agent_notes or "No agent notes were provided."

    return f"""Customer message:
{customer_message}

Agent notes:
{notes}

Return:
1. A short case summary in 2-4 sentences.
2. Up to three concrete next actions.
"""
