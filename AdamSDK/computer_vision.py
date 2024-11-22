import requests

class Vision:
    def __init__(self, server_url="http://localhost:5000"):
        self.server_url = server_url

    def pose_estimation(self, status=None, draw=None):
        url = f"{self.server_url}/pose_estimation"
        payload = {"status": status, "draw": draw}
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            data = response.json()
            return data.get("landmarks", None)
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error in pose estimation: {e}")

    def face_recognition(self, status=None, draw=None):
        url = f"{self.server_url}/face_recognition"
        payload = {"status": status, "draw": draw}
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            data = response.json()
            return data.get("faces", None)
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error in face recognition: {e}")

    def person_tracking(self, status=None, draw=None, tracking=None, direction=None):
        url = f"{self.server_url}/person_tracking"
        payload = {"status": status, "draw": draw, "tracking": tracking, "direction": direction}
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            data = response.json()
            centroids = data.get("centroids", None)
            directions = data.get("directions", None)
            return centroids, directions
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error in person tracking: {e}")
