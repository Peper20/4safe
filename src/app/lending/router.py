import cv2


from fastapi import Depends, APIRouter, Request, WebSocket, WebSocketDisconnect
from websockets.exceptions import ConnectionClosedError
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from vidgear.gears import NetGear


from app.services.cv_detection import prepare_frame




router = APIRouter()


templates = Jinja2Templates(directory="templates")



@router.get('/', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})


@router.get('/login-register', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse('auth.html', {'request': request})

@router.get('/video-demo', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse('video_demo.html', {'request': request})


camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)

@router.websocket('/video')
async def get_stream(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            # client = NetGear(receive_mode=True)
            # client = NetGear(receive_mode=True)
            # frame = client.recv()
            success, frame = camera.read()

            if frame is None:
                break

            prepare_frame(frame)

            ret, buffer = cv2.imencode('.jpg', frame)
            await websocket.send_bytes(buffer.tobytes())

    except (WebSocketDisconnect, ConnectionClosedError):
        print("Client disconnected")

