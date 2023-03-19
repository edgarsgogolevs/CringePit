from typing import List

from fastapi import APIRouter, Depends
from tortoise.contrib.fastapi import HTTPNotFoundError

import src.crud.reviewsType as crud
from src.auth.jwthandler import get_current_user
from src.schemas.reviewsType import ReviewTypeInSchema, ReviewTypeOutSchema, UpdateReviewType
from src.schemas.token import Status

router = APIRouter()

@router.get(
    "/reviewType",
    response_model=List[ReviewTypeOutSchema],
    dependencies=[Depends(get_current_user)]
)
async def get_review_types():
    return await crud.get_review_types()

@router.post(
    "/reviewType",
    response_model=ReviewTypeOutSchema,
    dependencies=[Depends(get_current_user)]
)
async def create_review_type(
    reviewType: ReviewTypeInSchema,
) -> ReviewTypeOutSchema:
    return await crud.create_review_type(reviewType)

@router.patch(
    "/reviewType/{review_type_id}",
    dependencies=[Depends(get_current_user)],
    response_model=ReviewTypeOutSchema,
    responses={404: {"model": HTTPNotFoundError}},
)
async def update_review_type(
    review_id: int,
    review: UpdateReviewType,
) -> ReviewTypeOutSchema:
    return await crud.update_review_type(review_id, review)


@router.delete(
    "/reviewType/{review_type_id}",
    response_model=Status,
    responses={404: {"model": HTTPNotFoundError}},
    dependencies=[Depends(get_current_user)],
)
async def delete_review(
    review_type_id: int
):
    return await crud.delete_review_type(review_type_id)