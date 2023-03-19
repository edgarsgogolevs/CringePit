from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from src.database.models import Reviews
from src.schemas.reviews import ReviewOutSchema
from src.schemas.token import Status



async def get_reviews():
    return await ReviewOutSchema.from_queryset(Reviews.all())


async def get_review(review_id) -> ReviewOutSchema:
    return await ReviewOutSchema.from_queryset_single(Reviews.get(id=review_id))


async def create_review(review, current_user) -> ReviewOutSchema:
    review_dict = review.dict(exclude_unset=True)
    review_dict["author_id"] = current_user.id
    review_obj = await Reviews.create(**review_dict)
    return await ReviewOutSchema.from_tortoise_orm(review_obj)


async def update_review(review_id, review, current_user) -> ReviewOutSchema:
    try:
        db_review = await ReviewOutSchema.from_queryset_single(Reviews.get(id=review_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Review {review_id} not found")

    if db_review.author.id == current_user.id:
        await Reviews.filter(id=review_id).update(**review.dict(exclude_unset=True))
        return await ReviewOutSchema.from_queryset_single(Reviews.get(id=review_id))

    raise HTTPException(status_code=403, detail=f"Not authorized to update")


async def delete_review(review_id, current_user) -> Status:
    try:
        db_review = await ReviewOutSchema.from_queryset_single(Reviews.get(id=review_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Review {review_id} not found")

    if db_review.author.id == current_user.id:
        deleted_count = await Reviews.filter(id=review_id).delete()
        if not deleted_count:
            raise HTTPException(status_code=404, detail=f"Review {review_id} not found")
        return Status(message=f"Deleted Review {review_id}")
    raise HTTPException(status_code=403, detail=f"Not authorized to delete")
