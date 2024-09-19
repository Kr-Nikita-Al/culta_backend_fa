from typing import List

from Company.interfaces_response.get_company_response import GetCompanyResponse
from base_model_response import BaseModelResponse


class GetAllCompanyResponse(BaseModelResponse):
    companies: List[GetCompanyResponse]
