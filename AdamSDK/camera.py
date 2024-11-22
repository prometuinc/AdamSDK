import requests

class Camera:
    def __init__(self, server_url="http://localhost:5000"):
        self.server_url = server_url

    def control_camera(self, status=True, window=False, title="Adam Camera"):
        """
        Controls the camera, allows you to turn it on or off, show the window, and set a title.
        :param status: True to turn on, False to turn off.
        :param window: True to show the window, False to disable it.
        :param title: Title of the window.
        """
        url = f"{self.server_url}/control_camera"
        payload = {"status": status, "window": window, "title": title}
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error connecting to the server: {e}")