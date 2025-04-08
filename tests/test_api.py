import pytest
from app.Base import User
from app.fuctions import create_user, delete_user, get_user, update_user

# Get Method
@pytest.mark.asyncio
async def test_get_user():

    response = await get_user(2)
    user_data = response.json()
  
    assert response.status_code == 200
    assert user_data['data']['id'] == 2
    assert 'email' in user_data['data']

    print("\n Get Status Code : ",response.status_code)

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

# Update Method
@pytest.mark.asyncio
async def test_update_user():

    updated_user = User(name="Jane Doe", job="Senior Software Developer")
    response = await update_user(2, updated_user)
    updated_user_data_json = response.json()
   
    assert updated_user_data_json['name'] == updated_user.name
    assert updated_user_data_json['job'] == updated_user.job
    assert response.status_code == 200

    print(" Upadted Status Code : ",response.status_code)

# Delete Method
@pytest.mark.asyncio
async def test_delete_user():
    response = await delete_user(2)
    assert response.status_code == 204

    print(" Deleted User : ",response.status_code)