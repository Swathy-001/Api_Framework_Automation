import pytest
from app.Base import User
from app.fuctions import delete_user

# Delete Method
@pytest.mark.asyncio
async def test_delete_user():
    response = await delete_user(2)
    assert response.status_code == 204

    print(" Deleted User : ",response.status_code)