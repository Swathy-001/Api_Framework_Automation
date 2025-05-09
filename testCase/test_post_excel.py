import pytest
import requests
import openpyxl
from app.config import BASE_URL

# Read data from the Excel file
def read_excel_data(file_path):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    return [
        {
          'name': row[0],             
          'job': row[1],              
          'status_code': row[2] 
        }
   
        for row in sheet.iter_rows(min_row=2, values_only=True)
        if row[2] == 201
    ]
#Read From excel
file_path = read_excel_data('Test_Data.xlsx')


@pytest.mark.parametrize("data", file_path)
def test_post_request(data):
    response = requests.post(f"{BASE_URL}/users", json={"name": data["name"], "job": data["job"]})
    assert response.status_code == 201  
   

    if response.status_code == 201:
        json_response = response.json()
        assert json_response["name"] == data["name"]
        assert json_response["job"] == data["job"]
        assert "id" in json_response  
        print(response.json())
