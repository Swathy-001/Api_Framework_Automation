import pytest
from app.Base import User
from app.fuctions import create_user

# Post Method
@pytest.mark.asyncio
async def test_create_user():

    new_user = User(name="John Doe", job="Software Developer")
    response = await create_user(new_user)
    created_user = response.json()

    assert response.status_code == 201
    assert created_user['name'] == new_user.name
    assert created_user['job'] == new_user.job
    assert 'id' in created_user
    assert 'createdAt' in created_user

    print("Created Status Code : ",response.status_code)

