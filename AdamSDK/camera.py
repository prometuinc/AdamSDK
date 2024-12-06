import requests

class Camera:
    def __init__(self, server_url="http://localhost:5000"):
        self.server_url = server_url

    def camera_control(self, status=True):
        """
        Controls the camera (turn it on or off).
        :param status: True to turn on, False to turn off.
        """
        url = f"{self.server_url}/camera_control"
        payload = {"status": status}
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error connecting to the server: {e}")

    def camera_control_window(self, window=False, title="Adam Camera"):
        """
        Controls the camera window (show or hide) and sets the title.
        :param window: True to show the window, False to hide it.
        :param title: Title of the window.
        """
        url = f"{self.server_url}/camera_control_window"
        payload = {"window": window, "title": title}
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error connecting to the server: {e}")
