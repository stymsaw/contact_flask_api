import requests

url = 'https://contact-flask-api-3.vercel.app/submit'
data = {
    "name": "Md Azmattullah",
    "email": "john@example.com",
    "phone_no": "1234567890",
    "message": "Hello, this is a test message."
}
    
response = requests.post(url, json=data)

print(f'Status Code: {response.status_code}')
print('Response JSON:', response.json())