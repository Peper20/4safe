from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from .di import init_dependencies
from .routers import init_routers




def create_app() -> FastAPI:
	app = FastAPI()

	init_routers(app)
	init_dependencies(app)

	# allows cross-origin requests from React
	origins = [
		"http://localhost",
		"http://localhost:8000",
	]

	app.add_middleware(
		CORSMiddleware,
		allow_origins=origins,
		allow_credentials=True,
		allow_methods=["*"],
		allow_headers=["*"],
	)


	return app

