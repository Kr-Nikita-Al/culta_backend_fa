from datetime import time
from typing import Union, List
from uuid import UUID

from sqlalchemy import select, update, and_
from sqlalchemy.ext.asyncio import AsyncSession

from ProductCard.models.model_db import ProductCardDB


class ProductCardDal:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_product_card(self, title: str, sub_title: str, header: str, description: str, hint_header: str,
                                  hint_description: str, product_category: str, custom_product_category: str,
                                  product_release_type: str, allergens_list: str, quantity_system: str, tags: str,
                                  count_number: int, price_field_1: int, price_field_2: int, cost_price_field_1: int,
                                  cost_price_field_2: int, cashback_field_1: int, cashback_field_2: int,
                                  product_quantity: int, calorie_content: int, proteins: int, fats: int,
                                  carbohydrates: int, cooking_time: int, bonuses_payment: bool,
                                  single_product_type: bool, is_sharpness: bool, is_hotness: bool,
                                  company_group_id: int, product_image_id: str, icon_image_id: str) -> ProductCardDB:
        new_company = ProductCardDB(
            title=title,
            sub_title=sub_title,
            header=header,
            description=description,
            hint_header=hint_header,
            hint_description=hint_description,
            product_category=product_category,
            custom_product_category=custom_product_category,
            product_release_type=product_release_type,
            allergens_list=allergens_list,
            quantity_system=quantity_system,
            tags=tags,
            count_number=count_number,
            price_field_1=price_field_1,
            price_field_2=price_field_2,
            cost_price_field_1=cost_price_field_1,
            cost_price_field_2=cost_price_field_2,
            cashback_field_1=cashback_field_1,
            cashback_field_2=cashback_field_2,
            product_quantity=product_quantity,
            calorie_content=calorie_content,
            proteins=proteins,
            fats=fats, carbohydrates=carbohydrates,
            cooking_time=cooking_time,
            bonuses_payment=bonuses_payment,
            single_product_type=single_product_type,
            is_sharpness=is_sharpness,
            is_hotness=is_hotness,
            company_group_id=company_group_id,
            product_image_id=product_image_id,
            icon_image_id=icon_image_id
        )
        self.db_session.add(new_company)
        await self.db_session.flush()
        return new_company
