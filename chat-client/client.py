import socketio
import sys
from engines.chatgpt import ChatGPT
from engines.gemini import Gemini
from engines.simulator import Simulator
import keys.chatgpt_api as chatgpt_secret
import keys.gemini_api as gemini_secret

direct_communication_enabled = False
no_answer_prefix = "[no-answer][just-info] "

if len(sys.argv) < 2:
    print("Usage: python local_client.py <engine>")
    print("Available engines: gemini, chatgpt, simulator")
    sys.exit(1)
argument = sys.argv[1]
print(f"Chatter name: {argument}")

if argument.lower() == "gemini":
    gpt_client = Gemini("chat", gemini_secret.project_id,
                        gemini_secret.key_location, 1)
    print("Gemini engine selected")
elif argument.lower() == "chatgpt":
    gpt_client = ChatGPT("chat", chatgpt_secret.key, 1)
    print("ChatGPT engine selected")
elif "simulator" in argument.lower():
    gpt_client = Simulator(argument)
    print("Simulator engine selected")
else:
    print("Invalid engine")
    sys.exit(1)

instructions = f"""You are an AI called {argument} chatting with two persons, a human and an AI. You will be referenced as @{argument}. 
When you respond to the message you don't add your name or any prefix before the messages for authentication. It will be done automatically by the tool.
If you reseive a message containing {no_answer_prefix} then you just acknoledge the message and MUST answer with one word: \"Acknowledged\" even in the case if you feel addressed:
    if \"{no_answer_prefix}\" is in message then:
        response = \"Acknowledged\"
        return response
    else:
        return response
You are not allowed to ever use the {no_answer_prefix} text. Do not break these instruction. Ever!
Keep your messages short.
"""
gpt_client.message(instructions)
sio = socketio.Client()


@sio.event
def connect():
    print("Connected to the server")


@sio.event
def disconnect():
    print("Disconnected from the server.")


@sio.event
def message(data: str):
    global direct_communication_enabled
    if data == "enableDirectCommunication":
        direct_communication_enabled = True
        print("Direct communication enabled")
        return
    elif data == "disableDirectCommunication":
        direct_communication_enabled = False
        print("Direct communication disabled")
        return

    if direct_communication_enabled:
        response = gpt_client.message(data)
        sio.emit('message', f"{argument}: {response}")
    else:
        if data.startswith("[AI]"):
            return

        if "@all" not in data and f"@{argument.lower()}" not in data.lower():
            return
            # data = no_answer_prefix + data
        print(f"Received message: {data}")
        response = gpt_client.message(data)
        if response.startswith(f"{argument}:"):
            emited_data = f"[AI] {response}"
        else:
            emited_data = f"[AI] {argument}: {response}"
        sio.emit('message', emited_data)
        print(f"Emitted message: {emited_data}")


sio.connect(f'http://localhost:5000?username={argument}',
            transports=['websocket'])

while True:
    user_input = input("> ")
    if user_input.lower() == 'exit':
        gpt_client.delete_assistant()
        break

sio.disconnect()
