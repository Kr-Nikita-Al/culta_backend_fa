from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ProductCard.actions import __create_product_card
from ProductCard.intarface_response import CreateProductCardResponse
from ProductCard.interface_request import CreateProductCardRequest
from db.session import get_db

product_card_router = APIRouter()


@product_card_router.post('/create', response_model=CreateProductCardResponse)
async def create_product_card(body: CreateProductCardRequest, db: AsyncSession = Depends(get_db)) -> CreateProductCardResponse:
    return await __create_product_card(body, db)
