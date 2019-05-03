from fastapi import FastAPI

app = FastAPI()

# Method 1: Use the decorator
# @app.get("/")
# async def root():
#     return {"message": "Hello test"}

# Method 2: Call the decorator later
async def root():
    return {"message": "Hello test"}

app.get("/")(root)

# @app.get("/items/{item_id}")
# async def read_item(item_id):
#     return {"item_id": item_id}

# root()

# print(root)

