from typing import Union, List

from sqlalchemy.ext.asyncio import AsyncSession

from Company.db.model_dal import CompanyDal
from Company.db.model_db import CompanyDB


async def _get_all_companies(session: AsyncSession) -> Union[List[CompanyDB], None]:
    async with session.begin():
        company_dal = CompanyDal(session)
        companies = await company_dal.get_all_companies()
        return companies
