import sys
sys.path.append('/media/manoj/datadisk_linux/JARVIS-AGI/')

import asyncio
import base64
import os
import requests

import aiohttp
import aiofiles
from TOOLS.AUDIO import Interrupted_Playsound
# import playsound

class Async_Speechify_Speechify_SpeechGenerator:
    """
    A class to asynchronously convert text to speech using the Speechify API,
    leveraging aiohttp for faster response times. The speak method
    handles the asyncio event loop management internally.
    """

    def __init__(self, output_audio_file: str = "Assets/output_audio.mp3"):
        """
        Initializes the Async_Speechify_Speechify_SpeechGenerator with default parameters.

        Args:
            output_audio_file (str): The path to save the temporary audio output file.
        """
        self.output_audio_file = output_audio_file
        self.api_endpoint = "https://audio.api.speechify.com/generateAudioFiles"
        self.default_voice = "mrbeast"  # Set default voice name
        self.default_language = "en-US"

    def speak(self, text: str, voice_name: str = None) -> None:
        """
        Converts the given text to speech and plays the audio. Manages the
        asyncio event loop internally for a simplified calling pattern.

        Args:
            text (str): The text to be converted to speech.
            voice_name (str, optional): The desired voice for speech synthesis.
                Available options include:
                    - jamie
                    - mrbeast
                    - snoop
                    - henry
                    - gwyneth
                    - cliff
                    - narrator
                Defaults to the voice set in __init__.
        """
        asyncio.run(self._speak_async(text, voice_name))

    async def _speak_async(self, text: str, voice_name: str = None) -> None:
        """
        Asynchronous helper function to handle the actual speech synthesis and playback.
        """
        try:
            os.remove(self.output_audio_file)
        except FileNotFoundError:
            pass

        if voice_name is None:
            voice_name = self.default_voice

        request_payload = {
            "audioFormat": "mp3",
            "paragraphChunks": [text],
            "voiceParams": {
                "name": voice_name,
                "engine": "speechify",
                "languageCode": self.default_language
            }
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(self.api_endpoint, json=request_payload) as response:
                response.raise_for_status()
                response_data = await response.json()

        audio_data = base64.b64decode(response_data['audioStream'])

        async with aiofiles.open(self.output_audio_file, 'wb') as audio_file:
            await audio_file.write(audio_data)

        # playsound.playsound(self.output_audio_file)
        Interrupted_Playsound.play_audio(self.output_audio_file)
        os.remove(self.output_audio_file)

class Speechify_SpeechGenerator:
    """
    A class to convert text to speech using the Speechify API.
    """

    def __init__(self, output_audio_file: str = "Assets/output_audio.mp3"):
        """
        Initializes the Speechify_SpeechGenerator class with default parameters.

        Args:
            output_audio_file (str): The path to save the temporary audio output file.
        """
        self.output_audio_file = output_audio_file
        self.api_endpoint = "https://audio.api.speechify.com/generateAudioFiles"
        self.default_voice = "mrbeast"  # Set default voice name
        self.default_language = "en-US"

    def speak(self, text: str, voice_name: str = None) -> None:
        """
        Converts the given text to speech and plays the audio.

        Args:
            text (str): The text to be converted to speech.
            voice_name (str, optional): The desired voice for speech synthesis.
                Available options include:
                    - jamie
                    - mrbeast
                    - snoop
                    - henry
                    - gwyneth
                    - cliff
                    - narrator
                Defaults to the voice set in __init__.
        """
        try:
            os.remove(self.output_audio_file)
        except FileNotFoundError:
            pass

        if voice_name is None:
            voice_name = self.default_voice

        request_payload = {
            "audioFormat": "mp3",
            "paragraphChunks": [text],
            "voiceParams": {
                "name": voice_name,
                "engine": "speechify",
                "languageCode": self.default_language
            }
        }

        response = requests.post(self.api_endpoint, json=request_payload)
        response.raise_for_status()  # Raise an exception for bad status codes

        audio_data = base64.b64decode(response.json()['audioStream'])
        with open(self.output_audio_file, 'wb') as audio_file:
            audio_file.write(audio_data)

        # playsound.playsound(self.output_audio_file)
        Interrupted_Playsound.play_audio(self.output_audio_file)
        os.remove(self.output_audio_file)

def speak(paragraph: str, voice_name: str = "mrbeast", filename: str = "ASSETS/output_audio.mp3"):
    """
    Converts text to speech using the Speechify API and plays the audio.

    Parameters:
        paragraph (str): The text to convert to speech.
        voice_name (str): The voice model to use for speech generation.
                                    Available voices:
                                        - jamie
                                        - mrbeast
                                        - snoop
                                        - henry
                                        - gwyneth
                                        - cliff
                                        -narrator

        filename (str): The temporary file to save the audio output.
    """
    try: os.remove(filename)
    except: pass

    url = "https://audio.api.speechify.com/generateAudioFiles"
    payload = {
        "audioFormat": "mp3",
        "paragraphChunks": [paragraph],
        "voiceParams": {
            "name": voice_name,
            "engine": "speechify",
            "languageCode": "en-US"
        }
    }

    response = requests.post(url, json=payload)
    response.raise_for_status()

    audio_data = base64.b64decode(response.json()['audioStream'])
    with open(filename, 'wb') as audio_file:
        audio_file.write(audio_data)

    # playsound.playsound(filename)
    Interrupted_Playsound.play_audio(filename)
    os.remove(filename)

if __name__ == "__main__":
    speech_synthesizer = Async_Speechify_Speechify_SpeechGenerator()
    speech_synthesizer = Speechify_SpeechGenerator()

    # speech_synthesizer.speak("Thank you for watching! I hope you found this video informative and helpful. If you did, please give it a thumbs up and consider subscribing to my channel for more videos like this.", voice_name='jamie')
    # speech_synthesizer.speak("Thank you for watching! I hope you found this video informative and helpful. If you did, please give it a thumbs up and consider subscribing to my channel for more videos like this.", voice_name='henry')
    # speech_synthesizer.speak("Thank you for watching! I hope you found this video informative and helpful. If you did, please give it a thumbs up and consider subscribing to my channel for more videos like this.", voice_name='snoop')
    # speech_synthesizer.speak("Thank you for watching! I hope you found this video informative and helpful. If you did, please give it a thumbs up and consider subscribing to my channel for more videos like this.", voice_name='gwyneth')
    # speech_synthesizer.speak("Thank you for watching! I hope you found this video informative and helpful. If you did, please give it a thumbs up and consider subscribing to my channel for more videos like this.", voice_name='cliff')
    # speech_synthesizer.speak("Thank you for watching! I hope you found this video informative and helpful. If you did, please give it a thumbs up and consider subscribing to my channel for more videos like this.", voice_name='narrator')

    # speech_synthesizer.speak("Thank you for watching! I hope you found this video informative and helpful. If you did, please give it a thumbs up and consider subscribing to my channel for more videos like this.")



    # speak("Thank you for watching! I hope you found this video informative and helpful. If you did, please give it a thumbs up and consider subscribing to my channel for more videos like this.", voice_name='jamie')
    # speak("Thank you for watching! I hope you found this video informative and helpful. If you did, please give it a thumbs up and consider subscribing to my channel for more videos like this.", voice_name='henry')
    # speak("Thank you for watching! I hope you found this video informative and helpful. If you did, please give it a thumbs up and consider subscribing to my channel for more videos like this.", voice_name='snoop')
    # speak("Thank you for watching! I hope you found this video informative and helpful. If you did, please give it a thumbs up and consider subscribing to my channel for more videos like this.", voice_name='gwyneth')
    # speak("Thank you for watching! I hope you found this video informative and helpful. If you did, please give it a thumbs up and consider subscribing to my channel for more videos like this.", voice_name='cliff')
    # speak("Thank you for watching! I hope you found this video informative and helpful. If you did, please give it a thumbs up and consider subscribing to my channel for more videos like this.", voice_name='narrator')

    speak("India is a diverse country with a rich cultural heritage and the world's largest democracy. It's known for its historical sites, vibrant festivals, and delicious cuisine.")