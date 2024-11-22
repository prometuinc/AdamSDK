import requests

class RobotControl:
    def __init__(self, server_url="http://localhost:5000"):
        self.server_url = server_url

    def move_forward(self, speed=1):
        url = f"{self.server_url}/move_forward"
        params = {"speed": speed}
        try:
            response = requests.post(url, json=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error in move_forward request: {e}")

    def move_backward(self, speed=1):
        url = f"{self.server_url}/move_backward"
        params = {"speed": speed}
        try:
            response = requests.post(url, json=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error in move_backward request: {e}")

    def turn_left(self, speed=1):
        url = f"{self.server_url}/turn_left"
        params = {"speed": speed}
        try:
            response = requests.post(url, json=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error in turn_left request: {e}")

    def turn_right(self, speed=1):
        url = f"{self.server_url}/turn_right"
        params = {"speed": speed}
        try:
            response = requests.post(url, json=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error in turn_right request: {e}")
