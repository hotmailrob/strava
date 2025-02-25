import requests
from settings import Settings


auth_url = "https://www.strava.com/oauth/token"
settings = Settings()
payload = {
    'client_id': settings.CLIENT_ID,
    'client_secret': settings.CLIENT_SECRET,
    'code': settings.CODE,  # Replace with the code from step 2
    'grant_type': 'authorization_code',
    'redirect_uri': 'http://localhost/'
}
response = requests.post(auth_url, data=payload)
print(response.json())