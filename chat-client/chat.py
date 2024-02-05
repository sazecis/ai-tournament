from engines.gemini import Gemini
import keys.gemini_api as gemini_secret

ai = Gemini(gemini_secret.project_id, gemini_secret.key_location, 1)

while True:
    my_message = input("Csaba: ")
    print(ai.message(my_message))
