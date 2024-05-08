from fastapi import FastAPI
from contextlib import asynccontextmanager


from app.routers import niche, blog, tool
from app.database import connect


app = FastAPI()


@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect.connect_db.ping()
    yield
    await connect.connect_db.close()


app.include_router(niche.router, prefix="/niche", tags=["niches", "niche"])
app.include_router(blog.router, prefix="/blog", tags=["blogs", "blog"])
app.include_router(tool.router, prefix="/tool", tags=["tools", "tool"])