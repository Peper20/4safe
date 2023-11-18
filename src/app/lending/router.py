from typing import Any
import cv2
import websockets
import asyncio
import numpy as np


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




class Hendler:
    def __init__(self, future, websocket) -> None:
        self.future = future
        self.websocket = websocket
    
    async def __call__(self, client_websocket):
        frame_as_bytes = await client_websocket.recv()
        
        frame = frame = cv2.imdecode(np.frombuffer(frame_as_bytes, np.uint8), cv2.IMREAD_COLOR)

        if frame is None:
            self.future.set_result(True)
            self.future.done()

        prepare_frame(frame)

        ret, buffer = cv2.imencode('.jpg', frame)
        await self.websocket.send_bytes(buffer.tobytes())

@router.websocket('/video')
async def get_stream(websocket: WebSocket):
    await websocket.accept()
    try:
        future = asyncio.Future()
        async with websockets.serve(Hendler(websocket, websocket), "localhost", 8765):
            await asyncio.Future()  # run forever



    except (WebSocketDisconnect, ConnectionClosedError):
        print("Client disconnected")

    print('AAAAAAAAAAA !!!!!!')