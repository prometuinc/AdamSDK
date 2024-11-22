from sdk import AdamSDK
import time

# Create an instance of the SDK
adam = AdamSDK()

# Control the camera
adam.control_camera(status=True, window=True, title="Adam Vision")

while True:
    # Pose estimation
    pose_data = adam.pose_estimation(status=True, draw=True)
    print(f"Pose Data: {pose_data}")

    # Face recognition
    face_data = adam.face_recognition(status=True, draw=True)
    print(f"Face Data: {face_data}")

    # Person tracking
    person_tracking_data = adam.person_tracking(status=False, draw=False, direction=True)
    print(f"Person Tracking Data: {person_tracking_data}")

    # Wait for 1 second between iterations
    time.sleep(1)