import httpx
from app.Base import User
from app.config import BASE_URL

# Function to get a user by ID
async def get_user(user_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/users/{user_id}")
        if response.status_code != 200:
            raise Exception(f"Failed to get user with ID {user_id}, Status code: {response.status_code}")
        return response

# Function to create a new user
async def create_user(user: User):
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{BASE_URL}/users", json=user.model_dump())
        if response.status_code != 201: 
            raise Exception(f"Failed to create user, Status code: {response.status_code}")
        return response

# Function to update a user by ID
async def update_user(user_id: int, user: User):
    async with httpx.AsyncClient() as client:
        response = await client.put(f"{BASE_URL}/users/{user_id}", json=user.model_dump())
        if response.status_code != 200: 
            raise Exception(f"Failed to update user with ID {user_id}, Status code: {response.status_code}")
        return response
    
# Function to delete user
async def delete_user(user_id: int):
    async with httpx.AsyncClient() as client:
        response = await client.delete(f"{BASE_URL}/users/{user_id}")
        if response.status_code != 204: 
            raise Exception(f"Failed to delete user with ID {user_id}, Status code: {response.status_code}")
        return response