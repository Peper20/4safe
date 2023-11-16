from fastapi import Depends, APIRouter


from .schemas import UserCreate, UserRead, UserUpdate
from .dependencies import auth_backend, fastapi_users




router = APIRouter()


router.include_router(
	fastapi_users.get_auth_router(auth_backend),
	prefix='/auth/jwt',
	tags=['auth'],
)
router.include_router(
	fastapi_users.get_register_router(UserRead, UserCreate),
	prefix='/auth',
	tags=['auth'],
)
router.include_router(
	fastapi_users.get_reset_password_router(),
	prefix='/auth',
	tags=['auth'],
)
router.include_router(
	fastapi_users.get_verify_router(UserRead),
	prefix='/auth',
	tags=['auth'],
)
router.include_router(
	fastapi_users.get_users_router(UserRead, UserUpdate),
	prefix='/users',
	tags=['users'],
)

