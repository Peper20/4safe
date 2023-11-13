from fastapi import FastAPI


from app.auth import router as auth_router




def init_routers(app: FastAPI) -> None:
	app.include_router(auth_router)
