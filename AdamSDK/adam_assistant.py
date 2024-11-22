import requests

class Assistant:
    def __init__(self, server_url="http://localhost:5000"):
        self.server_url = server_url

    # Función para Speech-to-Text
    def sst(self, audio_file):
        url = f"{self.server_url}/sst"
        try:
            with open(audio_file, 'rb') as file:
                files = {'file': file}
                response = requests.post(url, files=files)
                response.raise_for_status()
                return response.json()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error in speech-to-text request: {e}")

    # Función para Text-to-Speech
    def tts(self, text):
        url = f"{self.server_url}/tts"
        payload = {"text": text}
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error in text-to-speech request: {e}")

    # Función para detección de wake word (escuchar y activar el robot)
    def listen_for_wake_word(self, wake_word="hey adam", audio_device="default"):
        # Esta función está esperando que el servidor esté en un endpoint que reciba el audio
        # y responda cuando detecte el wake word. Aquí asumo que se está procesando el audio
        # en el servidor y, cuando el wake word es reconocido, se vuelve a activar el SDK.

        url = f"{self.server_url}/listen"
        params = {"wake_word": wake_word, "audio_device": audio_device}
        try:
            response = requests.post(url, json=params)
            response.raise_for_status()
            data = response.json()
            if data.get("detected", False):
                print("Wake word detected! Activating assistant...")
                return True  # El wake word fue detectado
            return False  # El wake word no fue detectado
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error in wake word detection request: {e}")

    # Función para interactuar con el chat generativo
    def chat(self, user_input):
        url = f"{self.server_url}/chat"
        payload = {"message": user_input}
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            return response.json()  # Devuelve la respuesta generada por el servidor
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error in chat request: {e}")
