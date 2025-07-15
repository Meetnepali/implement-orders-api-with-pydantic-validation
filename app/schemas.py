from pydantic import BaseModel, Field, EmailStr, constr
from typing import Optional

class FeedbackBase(BaseModel):
    name: constr(min_length=1, max_length=50)
    email: EmailStr
    product: constr(min_length=1, max_length=100)
    rating: int = Field(..., ge=1, le=5, description="Rating must be between 1 and 5")
    comments: Optional[constr(max_length=500)] = None

class FeedbackCreate(FeedbackBase):
    pass

class FeedbackRead(FeedbackBase):
    id: int

    class Config:
        from_attributes = True
