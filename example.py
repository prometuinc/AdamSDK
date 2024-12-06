from sdk import AdamSDK
import time

# Create an instance of the SDK
adam = AdamSDK()

# Control the camera
# Llamada para controlar la cámara
adam.camera_control(status=True)

# Llamada para controlar la ventana
adam.camera_control_window(window=True, title="Adam Vision")

while True:
    # Pose estimation
    #pose_data = adam.pose_estimation(status=False, draw=True)
    #print(f"Pose Data: {pose_data}")

    # Face recognition
    #face_data = adam.face_recognition(status=False, draw=True)
    #print(f"Face Data: {face_data}")

    # Person tracking
    #person_tracking_data = adam.person_tracking(status=False, draw=True, direction=True)
    #print(f"Person Tracking Data: {person_tracking_data}")

    # Wait for 1 second between iterations
    time.sleep(1)