import uvicorn
from fastapi import FastAPI, APIRouter

import settings
from Company import company_router
from ProductCard import product_card_router
from navigations.Screen import screen_router
from utils.api.ping import service_router

#############################
# БЛОК ОПИСАНИЯ API ROUTES  #
#############################

# Создание приложения
app = FastAPI(title="culta_backend_fa")

# Создаем основной роутер
main_api_router = APIRouter()

# Подключение роутеров
main_api_router.include_router(company_router, prefix="/company", tags=["company"])
main_api_router.include_router(service_router, tags=["ping"])
main_api_router.include_router(screen_router, prefix="/screen", tags=['screen'])
main_api_router.include_router(product_card_router, prefix="/product_card", tags=['product_card'])

# Добавляем роутер в приложение
app.include_router(main_api_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=settings.APP_PORT)
