# day01 python error handling

## Goal
Handle ZeroDivisionError, ValueError, TypeError and create a safe division function. Add examples for success and failure. Run with python3 error_handling.py.

## Your checklist
- [x] Understand the concept
- [x] Write the implementation yourself
- [x] Run the code locally
- [x] Test a success case and an error case
- [x] Commit your work with a meaningful message

## Learning notes
- Multiple `except` clauses are evaluated top-down — the first one that matches wins, so order from most specific to most general.
- `ZeroDivisionError` catches `x / 0`; `TypeError` catches `"10" / 2` because `/` is not defined between `str` and `int`.
- `finally` runs whether the try block succeeded, raised, or returned early — useful for cleanup (closing files, releasing locks).
- Catching bare `Exception` is a code smell: it swallows everything including `KeyboardInterrupt` subtleties and hides real bugs. Catch the specific exception you can actually recover from.
- Never silently `except: pass` — at minimum log the error so a human can see what happened.
