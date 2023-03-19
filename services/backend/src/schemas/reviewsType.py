from typing import Optional

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import ReviewType

ReviewTypeInSchema = pydantic_model_creator(
    ReviewType, name="ReviewTypeIn", exclude_readonly=True
    )
ReviewTypeOutSchema = pydantic_model_creator(
    ReviewType, name="ReviewTypeOut", exclude=["reviews"]
    )

class UpdateReviewType(BaseModel):
    title: Optional[str]
