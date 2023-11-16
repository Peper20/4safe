from fastapi import FastAPI


from app.auth import router as auth_router
from app.lending import router as lending_router




def init_routers(app: FastAPI) -> None:
	app.include_router(auth_router)
	app.include_router(lending_router)
