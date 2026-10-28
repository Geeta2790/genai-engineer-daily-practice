
import logging
from fastapi import FastAPI, HTTPException

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

app = FastAPI()


@app.get("/health")
def health():
    logger.info("Health endpoint called")
    return {"status": "healthy"}


@app.get("/divide")
def divide(a: float, b: float):
    logger.info("Division request received")

    try:
        result = a / b

    except ZeroDivisionError:
        logger.warning("Division by zero attempted")
        raise HTTPException(
            status_code=400,
            detail="Cannot divide by zero"
        )

    except Exception:
        logger.exception("Unexpected division error")
        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )

    logger.info("Division completed successfully")
    return {"result": result}
