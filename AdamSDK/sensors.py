import requests

class Sensors:
    def __init__(self, server_url="http://localhost:5000"):
        self.server_url = server_url

    def get_temperature(self):
        url = f"{self.server_url}/get_temperature"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error in temperature request: {e}")

    def get_gyro(self):
        url = f"{self.server_url}/get_gyro"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error in gyro request: {e}")

    def get_accelerometer(self):
        url = f"{self.server_url}/get_accelerometer"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error in accelerometer request: {e}")
