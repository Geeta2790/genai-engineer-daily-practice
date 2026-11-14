# day02 fastapi logging

## Goal
Build a small FastAPI endpoint. Add Python logging with INFO, WARNING and ERROR. Test in Swagger and inspect terminal logs.

## Your checklist
- [x] Understand the concept
- [x] Write the implementation yourself
- [x] Run the code locally
- [x] Test a success case and an error case
- [x] Commit your work with a meaningful message

## Learning notes
- Log levels in order of severity: `DEBUG < INFO < WARNING < ERROR < CRITICAL`. `basicConfig(level=INFO)` shows INFO and above.
- `logger.exception("...")` is like `error()` but also appends the traceback — use it inside `except` blocks so you don't lose the stack.
- `logger.warning` for recoverable client errors (bad input, 4xx); `logger.exception` for unexpected server errors (5xx).
- `HTTPException(status_code=400, detail=...)` becomes a proper JSON error response — never leak a raw stack trace to the client.
- One logger per module via `logging.getLogger(__name__)` gives you "which file logged this?" for free in the output.
- Run: `uvicorn main:app --reload` — Swagger UI at `http://localhost:8000/docs`.
