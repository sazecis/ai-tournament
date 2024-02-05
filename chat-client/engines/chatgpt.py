from openai import OpenAI
import time


class ChatGPT:

    wait_time = 1

    last_message_from_assistant = None
    last_message_id = None

    def __init__(self, game, key, wait_time):
        self.client = OpenAI(
            api_key=key)
        self.assistant = self.create_assistant(game)
        self.thread = self.create_thread()
        self.wait_time = wait_time

    def create_thread(self):
        return self.client.beta.threads.create()

    def create_assistant(self, game):
        return self.client.beta.assistants.create(
            name=game,
            model="gpt-4",
            description=f"A {game} game",
            instructions=f"You are an AI chat. Following instructions will come.")

    def message(self, content):
        self.client.beta.threads.messages.create(
            thread_id=self.thread.id,
            role="user",
            content=content
        )
        run = self.client.beta.threads.runs.create(
            thread_id=self.thread.id,
            assistant_id=self.assistant.id
        )
        self.wait_for_assistant(run)
        message = None
        waiter = 1
        while message == None or message == "":
            message = self.get_last_message()
            print("Waiting for ChatGPT's message.")
            time.sleep(self.wait_time * waiter)
            waiter += 1
        message = f"ChatGPT: {message}"
        time.sleep(self.wait_time)
        return message

    def list_messages(self):
        messages = self.client.beta.threads.messages.list(
            thread_id=self.thread.id
        )
        for message in messages.data:
            for content in message.content:
                print(f"{message.role}: {content.text.value}")

    def wait_for_assistant(self, run):
        while True:
            run = self.client.beta.threads.runs.retrieve(
                thread_id=self.thread.id,
                run_id=run.id
            )
            messages = self.client.beta.threads.messages.list(
                thread_id=self.thread.id,
                order="desc",
            )
            message = messages.data[0]
            if message.role == "assistant":
                if self.last_message_from_assistant == None:
                    self.last_message_from_assistant = message.content[0].text.value
                    self.last_message_id = message.id
                    return
                elif self.last_message_id != message.id:
                    self.last_message_from_assistant = message.content[0].text.value
                    self.last_message_id = message.id
                    return
                else:
                    print("Waiting for ChatGPT assistant.")
            time.sleep(1)

    def get_last_message(self):
        messages = self.client.beta.threads.messages.list(
            thread_id=self.thread.id,
            order="desc"
        )
        for message in messages.data:
            for content in message.content:
                return content.text.value
        return None

    def delete_assistant(self):
        self.client.beta.assistants.delete(
            assistant_id=self.assistant.id
        )
        self.client.beta.threads.delete(
            thread_id=self.thread.id
        )
