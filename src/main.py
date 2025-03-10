from fastapi import FastAPI, Depends, HTTPException
from .api import users, items
from .services.auth import get_current_user
import uvicorn

app = FastAPI(title="Sample API", version="0.1.0")

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(
    items.router,
    prefix="/items",
    tags=["items"],
    dependencies=[Depends(get_current_user)]
)

@app.get("/")
async def root():
    return {"message": "Welcome to the Sample API"}

if __name__ == "__main__":
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)