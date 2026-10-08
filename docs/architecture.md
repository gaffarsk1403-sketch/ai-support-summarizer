# Architecture

## Flow

1. A user enters a customer message and optional agent notes in the React UI.
2. The UI calls the FastAPI `/summarize` endpoint.
3. Pydantic validates the incoming request.
4. The prompt service combines the user content with concise summarization instructions.
5. The LLM service calls the configured model and requests a structured JSON result.
6. The API validates the response shape and returns a summary plus next actions to the UI.

## Design goals

- keep model-specific logic outside the API layer;
- keep prompts versionable and easy to review;
- validate inputs before sending them to a model;
- handle malformed model output without crashing the API;
- avoid placing secrets in source control;
- make the system testable even without a live model API.

## Production improvements

A production implementation could add authentication, PII redaction, prompt versioning, response schemas, automated LLM evaluations, tracing, cost/latency metrics, retries, fallback models, caching, and human review for high-risk workflows.
