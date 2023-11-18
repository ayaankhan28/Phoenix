api_key = "*****"


import os
import openai
import pygame
def speak(content):
    os.environ["OPENAI_API_KEY"] = api_key#set  OPENAI_API_KEY=your_actual_api_key

    client = openai.OpenAI()#initializes an OpenAI client
    speech_file_path = "audio.mp3"
    response = client.audio.speech.create(
    model="tts-1",
    voice="alloy", input=f"{content}")
    response.stream_to_file(speech_file_path)#
    pygame.init()
    def play_mp3(file_path):
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

    mp3_file_path = 'audio.mp3'
    play_mp3(mp3_file_path)
    # Keep the program running while the music plays
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    # Adjust the time as needed
    pygame.mixer.quit()




