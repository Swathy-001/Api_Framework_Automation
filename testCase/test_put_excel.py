import pytest
import requests
import openpyxl
from app.config import BASE_URL

# Read data from the Excel file
def read_excel_data(file_path):
    sheet = openpyxl.load_workbook(file_path).active   
    return [
        {
          'name': row[0],             
          'job': row[1],              
          'status_code': row[2] 
        }
   
        for row in sheet.iter_rows(min_row=2, values_only=True)
        if row[2] == 200
    ]
      
    # return data
 
# Get data from the Excel file
test_data = read_excel_data('Test_Data.xlsx')

# Test Case for PUT request
@pytest.mark.parametrize("data", test_data)
def test_put_request(data):
    user_id = 2 
    response = requests.put(f"{BASE_URL}/users/{user_id}", json={"name": data["name"], "job": data["job"]})
   
    if response.status_code == 200:
        json_response = response.json()
        assert json_response["name"] == data["name"]
        assert json_response["job"] == data["job"]
    else:
        assert response.status_code == 404
    print(response.json())
    print(response.status_code)