from fastapi import Depends, APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates



router = APIRouter()


templates = Jinja2Templates(directory="templates")



@router.get('/', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@router.get('/login-register', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse('auth.html', {'request': request})

