from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import Users


UserInSchema = pydantic_model_creator(
    Users, name="UserIn", exclude=["movieReviews","created_at","modified_at", "reviews", "points", "yellow_cards", "red_cards", "id"]
)
UserOutSchema = pydantic_model_creator(
    Users, name="UserOut", exclude=["password", "created_at", "modified_at"]
)
UserDatabaseSchema = pydantic_model_creator(
    Users, name="User", exclude=["created_at", "modified_at"]
)