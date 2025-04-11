import pytest
from app.Base import User
from app.fuctions import update_user

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
