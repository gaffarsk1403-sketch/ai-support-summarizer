# AI Support Summarizer

An end-to-end AI-powered support workflow that turns long customer messages and agent notes into concise internal summaries and actionable next steps.

This project demonstrates how I structure an LLM feature across a React frontend, FastAPI backend, prompt orchestration layer, validation, testing, CI, and deployment-ready packaging.

## What it does

A support user enters:

- a customer message;
- optional internal agent notes.

The application:

1. validates the request;
2. sends the case through a prompt orchestration layer;
3. asks the LLM for a factual summary and up to three next actions;
4. handles malformed model output safely;
5. returns the result to the React UI.

## Tech stack

- React
- TypeScript
- FastAPI
- Python
- OpenAI API
- Pydantic
- Pytest
- Docker
- GitHub Actions

## Architecture

```text
React UI
   |
   v
FastAPI /summarize
   |
   +--> Pydantic validation
   |
   +--> Prompt orchestration
   |
   +--> LLM service
   |
   v
Summary + next actions
```

See [docs/architecture.md](docs/architecture.md) for design details and production hardening ideas.

## Backend setup

### 1. Create a virtual environment

```bash
python -m venv .venv
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Copy `.env.example` and provide an API key:

```text
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-4o-mini
```

### 4. Run the API

```bash
uvicorn backend.main:app --reload
```

The API documentation is available at `http://localhost:8000/docs`.

## Frontend setup

```bash
cd frontend
npm install
npm run dev
```

The frontend expects the backend at `http://localhost:8000`.

## Example API request

```json
{
  "case_id": "CASE-1001",
  "customer_message": "My payment was charged twice and I need help.",
  "agent_notes": "Customer contacted support this morning."
}
```

Example response:

```json
{
  "case_id": "CASE-1001",
  "summary": "The customer reports a duplicate payment charge and is requesting assistance.",
  "next_actions": [
    "Verify the duplicate transaction.",
    "Confirm the refund or adjustment path.",
    "Update the customer with the resolution."
  ]
}
```

## Testing

```bash
pytest
```

Tests verify the health endpoint and the non-LLM fallback behavior.

## CI

A GitHub Actions workflow runs backend tests on pushes to `main` and on pull requests.

## Docker

```bash
docker build -t ai-support-summarizer .
docker run -p 8000:8000 --env-file .env ai-support-summarizer
```

## Engineering decisions

- **Prompt isolation:** prompt construction is kept out of the API controller.
- **Input validation:** request sizes and required fields are validated before model execution.
- **Graceful failure:** the service does not crash when no API key is configured.
- **Structured responses:** summaries and next actions are returned as an explicit API contract.
- **Testability:** core API behavior can be tested without making a live model call.
- **No proprietary data:** all examples are synthetic and safe for a public portfolio.

## Production improvements

A production version could add:

- structured response schemas;
- PII redaction;
- prompt versioning;
- LLM evaluation datasets;
- human review for sensitive cases;
- tracing and model latency metrics;
- token/cost monitoring;
- retry and fallback strategies;
- authentication and role-based access;
- persistent case history.

## Why I built this

I wanted to demonstrate an AI feature beyond a single prompt call. This project shows the full path from a user-facing workflow to API validation, prompt design, model integration, output handling, automated testing, and deployment practices.

This repository is a portfolio project and contains no employer code, proprietary data, or confidential business logic.
