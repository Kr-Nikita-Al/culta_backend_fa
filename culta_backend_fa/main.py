import uvicorn
from fastapi import FastAPI, APIRouter

import settings
from Company.api_handlers import company_router
from Service.api.ping import service_router

#############################
# БЛОК ОПИСАНИЯ API ROUTES  #
#############################

# Создание приложения
app = FastAPI(title="culta_backend_fa")

# Создаем основной роутер
main_api_router = APIRouter()

# Добавляем роутер класс User (теперь стучаться только с роутом user)
main_api_router.include_router(company_router, prefix="/company", tags=["company"])
main_api_router.include_router(service_router, tags=["ping"])

# Добавляем роутер в приложение
app.include_router(main_api_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=settings.APP_PORT)