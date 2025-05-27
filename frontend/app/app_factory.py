from fastapi import FastAPI

from routers.main_page_routers import router
from settings import settings



def get_application() -> FastAPI:
    app = FastAPI(root_path_in_servers=True, debug=settings.DEBUG)
    app.include_router(router)

    return app
