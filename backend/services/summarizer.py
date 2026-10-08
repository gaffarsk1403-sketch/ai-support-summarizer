import json
import os

from openai import OpenAI

from backend.services.prompts import SYSTEM_PROMPT, build_case_prompt


def summarize_case(customer_message: str, agent_notes: str | None) -> tuple[str, list[str]]:
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        summary = customer_message.strip()
        if len(summary) > 220:
            summary = summary[:217].rstrip() + "..."
        return summary, ["Review the case details and determine the next support action."]

    client = OpenAI(api_key=api_key)
    model = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

    response = client.responses.create(
        model=model,
        instructions=SYSTEM_PROMPT,
        input=build_case_prompt(customer_message, agent_notes)
        + '\nReturn valid JSON with keys "summary" and "next_actions".',
    )

    text = response.output_text.strip()

    try:
        payload = json.loads(text)
        summary = str(payload["summary"]).strip()
        actions = [str(item).strip() for item in payload.get("next_actions", [])][:3]
        return summary, actions
    except (json.JSONDecodeError, KeyError, TypeError):
        return text, []
