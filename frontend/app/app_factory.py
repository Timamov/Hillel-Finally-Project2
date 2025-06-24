from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers.main_page_routers import router
from settings import settings



def get_application() -> FastAPI:
    app = FastAPI(root_path_in_servers=True, debug=settings.DEBUG)
    app.include_router(router)
    app.mount('/static', StaticFiles(directory='/static'), name='static')
    return app
