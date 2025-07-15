from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.status import HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
from fastapi.exceptions import RequestValidationError

class FeedbackNotFound(Exception):
    def __init__(self, feedback_id: int):
        self.feedback_id = feedback_id

async def feedback_not_found_handler(request: Request, exc: FeedbackNotFound):
    return JSONResponse(
        status_code=HTTP_404_NOT_FOUND,
        content={"detail": f"Feedback with id {exc.feedback_id} not found."}
    )

async def custom_validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=HTTP_400_BAD_REQUEST,
        content={"detail": "Invalid data provided.", "errors": exc.errors()},
    )
