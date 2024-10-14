import requests

data = {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "message": "This is a test message"
}

response = requests.post('http://127.0.0.1:8000/api/submit-form/', json=data)
print(response.status_code)
print(response.json())
