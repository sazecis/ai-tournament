import vertexai
from vertexai.preview.generative_models import GenerativeModel, ChatSession
import os
import time


class Gemini:

    wait_time = 1

    def __init__(self, project_id, key_location, wait_time):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_location
        location = "us-central1"
        vertexai.init(project=project_id, location=location)

        model = GenerativeModel("gemini-pro")
        self.chat = model.start_chat()
        self.wait_time = wait_time

    def message(self, user_input):
        prompt = user_input
        waiter = 1
        while True:
            try:
                response = self.chat.send_message(prompt)
                break
            except vertexai.generative_models._generative_models.ResponseBlockedError:
                print("Gemini send message blocked. Retrying.")
                time.sleep(self.wait_time * waiter)
                waiter += 1
        message = f"Gemini: {response.candidates[0].content.parts[0].text}"
        time.sleep(self.wait_time)
        return message

    def delete_assistant():
        return
