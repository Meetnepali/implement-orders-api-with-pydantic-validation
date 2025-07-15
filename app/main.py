import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from app.routers import feedback
from app import db, error_handlers
from fastapi.exceptions import RequestValidationError

load_dotenv()

app = FastAPI(title="Product Feedback API")

# CORS for development/demo; can restrict as needed
env = os.environ.get("APP_ENV", "development")
if env == "development":
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# DB setup
@app.on_event("startup")
def startup():
    db.Base.metadata.create_all(bind=db.engine)

# Routers
app.include_router(feedback.router)

# Error handlers
app.add_exception_handler(error_handlers.FeedbackNotFound, error_handlers.feedback_not_found_handler)
app.add_exception_handler(RequestValidationError, error_handlers.custom_validation_exception_handler)
