from uuid import UUID
from fastapi import APIRouter
from fastapi import Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from Company.actions import __create_company, __delete_company, __get_all_companies, __get_company_by_id, \
                            __update_company_by_id
from Company.interface_request import CreateCompanyRequest, UpdateCompanyRequest
from Company.interface_response import CreateCompanyResponse, DeleteCompanyResponse, GetAllCompanyResponse, \
                                       GetCompanyResponse, UpdateCompanyResponse
from db.session import get_db


company_router = APIRouter()


@company_router.post("/create", response_model=CreateCompanyResponse)
async def create_company(body: CreateCompanyRequest, db: AsyncSession = Depends(get_db)) -> CreateCompanyResponse:
    return await __create_company(body, db)


@company_router.delete("/delete", response_model=DeleteCompanyResponse)
async def delete_company(company_id: UUID, db: AsyncSession = Depends(get_db)) -> DeleteCompanyResponse:
    company_for_deletion = await __get_company_by_id(company_id=company_id, session=db)
    if company_for_deletion is None:
        raise HTTPException(status_code=404,
                            detail='Company with id {0} is not found'.format(company_id))
    # Попытка удалить пользователя
    deleted_company_id = await __delete_company(company_id, db)
    if deleted_company_id is None:
        raise HTTPException(status_code=404,
                            detail='Company with id {0} was deleted before'.format(company_id))
    return DeleteCompanyResponse(deleted_company_id=deleted_company_id)


@company_router.get('/get_by_id', response_model=GetCompanyResponse)
async def get_company_by_id(company_id: UUID, db: AsyncSession = Depends(get_db)) -> GetCompanyResponse:
    company = await __get_company_by_id(company_id, db)
    if company is None:
        raise HTTPException(status_code=404,
                            detail='Company with id {0} is not found or was deleted before'.format(company_id))
    return company


@company_router.get('/get_all', response_model=GetAllCompanyResponse)
async def get_all_companies(db: AsyncSession = Depends(get_db)) -> GetAllCompanyResponse:
    companies = await __get_all_companies(db)
    if companies is None:
        raise HTTPException(status_code=404,
                            detail='Table Company is empty')
    return GetAllCompanyResponse(companies=companies)


@company_router.patch('/update_by_id', response_model=UpdateCompanyResponse)
async def update_company_by_id(company_id: UUID,
                               body: UpdateCompanyRequest,
                               db: AsyncSession = Depends(get_db)) -> UpdateCompanyResponse:
    # Проверка на существование обновляемого пользователя
    company_for_update = await __get_company_by_id(company_id=company_id, session=db)
    if company_for_update is None:
        raise HTTPException(status_code=404,
                            detail='Company with id {0} is not found'.format(company_id))
    # Попытка обновить данные пользователя
    update_company_params = body.dict(exclude_none=True)  # exclude_none, чтобы удалить незаполненные поля
    if update_company_params == {}:
        raise HTTPException(status_code=422, detail='All fields are empty')
    try:
        updated_company_id = await __update_company_by_id(update_company_params=update_company_params,
                                                          company_id=company_id, session=db)
    except IntegrityError:
        raise HTTPException(status_code=503, detail='Database error')
    return UpdateCompanyResponse(updated_company_id=updated_company_id)
