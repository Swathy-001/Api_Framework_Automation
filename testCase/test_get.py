import pytest
from app.Base import User
from app.fuctions import get_user

# Get Method
@pytest.mark.asyncio
async def test_get_user():

    response = await get_user(2)
    user_data = response.json()
  
    assert response.status_code == 200
    assert user_data['data']['id'] == 2
    assert 'email' in user_data['data']

    print("\n Get Status Code : ",response.status_code)

