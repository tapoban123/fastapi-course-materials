from fastapi import FastAPI, WebSocket, Depends, HTTPException
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

from contextlib import asynccontextmanager
from fastapi.templating import Jinja2Templates
from fastapi import Request
from database import async_session, init_db
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession

from models import Notification
from schemas import NotificationCreate, NotificationRead
from fastapi.staticfiles import StaticFiles
from sqlalchemy import insert, select


async def get_session()->AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        yield session


# A simple connection manager to keep track of active websocket connections
class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []