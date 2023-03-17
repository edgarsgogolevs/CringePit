from typing import Optional

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import Reviews


ReviewInSchema = pydantic_model_creator(
    Reviews, name="ReviewIn", exclude=["author_id"], exclude_readonly=True)
ReviewOutSchema = pydantic_model_creator(
    Reviews, name="Review", exclude =[
      "modified_at", "author.password", "author.created_at", "author.modified_at"
    ]
)


class UpdateReview(BaseModel):
    title: Optional[str]
    content: Optional[str]
    type: Optional[int]