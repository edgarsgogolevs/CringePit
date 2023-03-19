from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from src.database.models import ReviewType
from src.schemas.reviewsType import ReviewTypeOutSchema
from src.schemas.token import Status

async def get_review_types():
    return await ReviewTypeOutSchema.from_queryset(ReviewType.all())

async def create_review_type(review_type) -> ReviewTypeOutSchema:
    review_type_dict = review_type.dict(exclude_unset=True)
    review_type_obj = await ReviewType.create(**review_type_dict)
    return await ReviewTypeOutSchema.from_tortoise_orm(review_type_obj)

async def update_review_type(review_type_id, review) -> ReviewTypeOutSchema:
    try:
        db_review_type = await ReviewTypeOutSchema.from_queryset_single(ReviewType.get(id=review_type_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Review type {review_type_id} not found")
    
    await ReviewType.filter(id=review_type_id).update(**review.dict(exclude_unset=True))
    return await ReviewTypeOutSchema.from_queryset_single(ReviewType.get(id=review_type_id))

async def delete_review_type(review_type_id) -> Status:
    try:
        db_review_type = await ReviewTypeOutSchema.from_queryset_single(ReviewType.get(id=review_type_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Review type {review_type_id} not found")
    
    deleted_count = await ReviewType.filter(id=review_type_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Review type {review_type_id} not found")
    return Status (message=f"Deleted Review type {review_type_id}") 