import requests

class Bluetooth:
    def __init__(self, server_url="http://localhost:5000"):
        self.server_url = server_url

    def list_devices(self):
        url = f"{self.server_url}/list_bluetooth_devices"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error in listing Bluetooth devices: {e}")

    def connect_device(self, device_id, password):
        url = f"{self.server_url}/connect_bluetooth_device"
        payload = {"device_id": device_id, "password": password}
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error in connecting Bluetooth device: {e}")

    def disconnect_device(self, device_id):
        url = f"{self.server_url}/disconnect_bluetooth_device"
        payload = {"device_id": device_id}
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error in disconnecting Bluetooth device: {e}")
