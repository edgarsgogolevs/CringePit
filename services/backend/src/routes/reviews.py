from typing import List

from fastapi import APIRouter, Depends, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import src.crud.reviews as crud
from src.auth.jwthandler import get_current_user
from src.schemas.reviews import ReviewOutSchema, ReviewInSchema, UpdateReview
from src.schemas.token import Status
from src.schemas.users import UserOutSchema


router = APIRouter()


@router.get(
    "/reviews",
    response_model=List[ReviewOutSchema],
    dependencies=[Depends(get_current_user)],
)
async def get_reviews():
    return await crud.get_review()


@router.get(
    "/reviews/{review_id}",
    response_model=ReviewOutSchema,
    dependencies=[Depends(get_current_user)],
)
async def get_review(review_id: int) -> ReviewOutSchema:
    try:
        return await crud.get_review(review_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Note does not exist",
        )


@router.post(
    "/reviews", response_model=ReviewOutSchema, dependencies=[Depends(get_current_user)]
)
async def create_review(
    review: ReviewInSchema, current_user: UserOutSchema = Depends(get_current_user)
) -> ReviewOutSchema:
    return await crud.create_review(review, current_user)


@router.patch(
    "/review/{review_id}",
    dependencies=[Depends(get_current_user)],
    response_model=ReviewOutSchema,
    responses={404: {"model": HTTPNotFoundError}},
)
async def update_review(
    review_id: int,
    review: UpdateReview,
    current_user: UserOutSchema = Depends(get_current_user),
) -> ReviewOutSchema:
    return await crud.update_review(review_id, review, current_user)


@router.delete(
    "/reviews/{review_id}",
    response_model=Status,
    responses={404: {"model": HTTPNotFoundError}},
    dependencies=[Depends(get_current_user)],
)
async def delete_review(
    review_id: int, current_user: UserOutSchema = Depends(get_current_user)
):
    return await crud.delete_review(review_id, current_user)