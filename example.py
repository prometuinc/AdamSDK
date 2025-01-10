from sdk import AdamSDK
import time

adam = AdamSDK() # Create an instance of the SDK

texto = "Hi, I'm Adam, your personal assistant. How can I help you today?"

# Text to speech
adam.tts(
    text=texto,
    idioma="en",
    genero="male",
    play=True,
    delete_after_play=True
)

# Control the camera
adam.camera_control(status=False)

# Open window
adam.camera_control_window(window=True, title="Adam Vision Window") 

while True:
    # Pose estimation
    pose_data = adam.pose_estimation(status=False, draw=True)
    #print(f"Pose Data: {pose_data}")

    face = adam.face_recognition(status=False, draw=True)


    person_tracking_data = adam.person_tracking(status=False, draw=True, direction=True)

    time.sleep(1)