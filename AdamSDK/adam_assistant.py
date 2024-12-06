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

    def tts(self, texto, idioma="en", genero="male", play=False, delete_after_play=False):
        """
        Convierte texto a voz usando el endpoint /tts.

        :param texto: El texto a convertir en audio.
        :param idioma: Idioma de la voz (ej. 'en' o 'es').
        :param genero: Género de la voz ('male' o 'female').
        :param play: Si es True, reproducirá el audio generado.
        :param delete_after_play: Si es True, eliminará el archivo después de reproducirlo.
        :return: Ruta del archivo de audio generado o mensaje de error.
        """
        url = f"{self.server_url}/tts"
        payload = {
            "texto": texto,
            "idioma": idioma,
            "genero": genero,
            "play": play,
            "delete_after_play": delete_after_play
        }

        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            return response.json()  # Devuelve la respuesta JSON del servidor
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

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
