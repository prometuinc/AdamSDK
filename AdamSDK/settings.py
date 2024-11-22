import requests

class Settings:
    def __init__(self, server_url="http://localhost:5000"):
        self.server_url = server_url

    def change_robot_name(self, new_name):
        url = f"{self.server_url}/change_robot_name"
        payload = {"name": new_name}
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error in changing robot name: {e}")
