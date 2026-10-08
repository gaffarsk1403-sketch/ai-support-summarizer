from fastapi import FastAPI

from backend.models import SummaryResponse, SupportCase
from backend.services.summarizer import summarize_case


app = FastAPI(
    title="AI Support Summarizer",
    version="1.0.0",
    description="LLM-powered support case summarization API.",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/summarize", response_model=SummaryResponse)
def summarize(case: SupportCase) -> SummaryResponse:
    summary, next_actions = summarize_case(
        customer_message=case.customer_message,
        agent_notes=case.agent_notes,
    )

    return SummaryResponse(
        case_id=case.case_id,
        summary=summary,
        next_actions=next_actions,
    )
