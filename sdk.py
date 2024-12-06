from AdamSDK.camera import Camera
from AdamSDK.computer_vision import Vision
from AdamSDK.adam_assistant import Assistant
from AdamSDK.robot import RobotControl
from AdamSDK.sensors import Sensors
from AdamSDK.bluetooth import Bluetooth
from AdamSDK.settings import Settings

class AdamSDK:
    def __init__(self, server_url="http://localhost:5000"):
        self.camera = Camera(server_url)
        self.vision = Vision(server_url)
        self.assistant = Assistant(server_url)
        self.robot = RobotControl(server_url)
        self.sensors = Sensors(server_url)
        self.bluetooth = Bluetooth(server_url)
        self.settings = Settings(server_url)

    def camera_control(self, status=True):
        """
        Controla el estado de la cámara y la ventana de OpenCV.
        """
        # Primero, controlamos la cámara
        return self.camera.camera_control(status)

    def camera_control_window(self, window=False, title="Camera Control"):
        """
        Controla la ventana de OpenCV.
        """
        return self.camera.camera_control_window(window, title)

    def pose_estimation(self, status=None, draw=None):
        return self.vision.pose_estimation(status, draw)

    def face_recognition(self, status=None, draw=None):
        return self.vision.face_recognition(status, draw)

    def person_tracking(self, status=None, draw=None, tracking=None, direction=None):
        return self.vision.person_tracking(status, draw, tracking, direction)

    def sst(self, audio_file):
        return self.assistant.sst(audio_file)

    def tts(self, text, idioma="en", genero="male", play=False, delete_after_play=False):
        """
        Convert text to speech using TTS functionality.

        :param text: The text to convert to audio.
        :param language: Language of the voice (e.g. 'en' or 'es').
        :param gender: Gender of the voice ('male' or 'female').
        :param play: If True, will play the generated audio.
        :param delete_after_play: If True, will delete the file after playing it.
        :return: Path of the generated audio file or error message.
        """
        return self.assistant.tts(
            texto=text,
            idioma=idioma,
            genero=genero,
            play=play,
            delete_after_play=delete_after_play,
        )

    def listen_for_wake_word(self, wake_word="hey adam", audio_device="default"):
        return self.assistant.listen_for_wake_word(wake_word, audio_device)

    def chat(self, user_input):
        return self.assistant.chat(user_input)

    def move_forward(self, speed=1):
        return self.robot.move_forward(speed)

    def move_backward(self, speed=1):
        return self.robot.move_backward(speed)

    def turn_left(self, speed=1):
        return self.robot.turn_left(speed)

    def turn_right(self, speed=1):
        return self.robot.turn_right(speed)

    def get_temperature(self):
        return self.sensors.get_temperature()

    def get_gyro(self):
        return self.sensors.get_gyro()

    def get_accelerometer(self):
        return self.sensors.get_accelerometer()

    def list_bluetooth_devices(self):
        return self.bluetooth.list_devices()

    def connect_bluetooth_device(self, device_id, password):
        return self.bluetooth.connect_device(device_id, password)

    def disconnect_bluetooth_device(self, device_id):
        return self.bluetooth.disconnect_device(device_id)

    def change_robot_name(self, new_name):
        return self.settings.change_robot_name(new_name)
