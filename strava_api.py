from typing import Any
import requests
from settings import Settings


class StravaAPI:
    access_token: str
    settings: Settings
    activities_url: str

    def __init__(self):
        self.settings = Settings()
        self.access_token = self._get_access_token()

    def _get_access_token(self) -> str:
        payload = {
            'client_id': self.settings.CLIENT_ID,
            'client_secret': self.settings.CLIENT_SECRET,
            'code': self.settings.CODE,
            'refresh_token': self.settings.REFRESH_TOKEN,
            'grant_type': 'refresh_token',
        }
        auth_url = "https://www.strava.com/oauth/token"
        response = requests.post(auth_url, data=payload)
        response.raise_for_status()
        return response.json()['access_token']

    def fetch_n_latest_activity_id(self, n=1) -> list[str]:
        activities_url = f"https://www.strava.com/api/v3/athlete/activities?page=1&per_page={n}"
        header = {'Authorization': f"Bearer {self.access_token}"}
        response = requests.get(activities_url, headers=header)
        response.raise_for_status()
        data = response.json()
        ids = []
        if data:
            for activity in data:
                ids.append(activity['id'])
        return ids

    def fetch_activity(self, activity_id: str) -> dict:
        header = {'Authorization': f"Bearer {self.access_token}"}
        activity_url = f"https://www.strava.com/api/v3/activities/{activity_id}?include_all_efforts=true"
        response = requests.get(activity_url, headers=header)
        response.raise_for_status()
        return response.json()

    def fetch_n_last_activities(self, n=1) -> list[dict]:
        ids = self.fetch_n_latest_activity_id(n)
        activities = []
        for activity_id in ids:
            activities.append(self.fetch_activity(activity_id))
        return activities
    
    def fetch_last_activity(self) -> dict:
        ids = self.fetch_n_latest_activity_id()
        return self.fetch_activity(ids[0])

    def update_activity_fields(self, activity_id: str, fields_to_update: list[tuple[str, Any]]) -> None:
        header = {'Authorization': f"Bearer {self.access_token}"}
        update_url = f"https://www.strava.com/api/v3/activities/{activity_id}"
        response = requests.put(update_url, headers=header, json={field[0]: field[1] for field in fields_to_update})
        response.raise_for_status()