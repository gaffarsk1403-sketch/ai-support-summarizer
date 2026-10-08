from pydantic import BaseModel, Field


class SupportCase(BaseModel):
    case_id: str = Field(min_length=1, max_length=100)
    customer_message: str = Field(min_length=5, max_length=5000)
    agent_notes: str | None = Field(default=None, max_length=5000)


class SummaryResponse(BaseModel):
    case_id: str
    summary: str
    next_actions: list[str]
