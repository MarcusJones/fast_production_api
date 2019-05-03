# first steps - using path decorators

from fastapi import FastAPI

app = FastAPI()

# Define the functions
async def root():
    return {"message": "Hello test"}

async def read_item(item_id):
    return {"item_id": item_id}

# Define the routes
app.get("/")(root)
app.get("/items/{item_id}")(read_item)

