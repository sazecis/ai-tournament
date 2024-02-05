from engines.chatgpt import ChatGPT
from engines.gemini import Gemini
from games.games import Games
import keys.chatgpt_api as chatgpt_secret
import keys.gemini_api as gemini_secret

WAIT_TIME = 1

not_supported_games = [Games.BlackJack]

game = Games.KnocKnock
game_name = game.game_name
game_rule = game.rule

chatgpt_client = ChatGPT(game_name, chatgpt_secret.key, WAIT_TIME)
gemini_client = Gemini(
    game_name, gemini_secret.project_id, gemini_secret.key_location, WAIT_TIME)


def main():
    if game in not_supported_games:
        print("This game is not supported in this application where the two players compete directly with each other without a dealer.")
        return
    print(f"Welcome to the {game_name} game!")
    welcome_chatgpt = intro_message("John", "Gemini", "ChatGPT")
    chatgpt_client.message(welcome_chatgpt)
    welcome_gemini = intro_message("John", "ChatGPT", "Gemini")
    answer_b = gemini_client.message(welcome_gemini)
    try:
        while True:
            try:
                while True:
                    answer_a = chatgpt_client.message(answer_b)
                    answer_b = gemini_client.message(answer_a)
            except KeyboardInterrupt:
                referee_message = "Stop! The referee is pausing the tournament. To provide some clarifications."
                print(referee_message)
                chatgpt_client.message(referee_message)
                gemini_client.message(referee_message)
            referee_input = input("Referee: ")
            answer_to_referee_chatgpt = f"Reaction of the other player: {chatgpt_client.message(referee_input)}"
            answer_to_referee_gemini = f"Reaction of the other player: {gemini_client.message(referee_input)}"
            chatgpt_client.message(answer_to_referee_gemini)
            answer_b = gemini_client.message(answer_to_referee_chatgpt)
    except KeyboardInterrupt:
        print("Exiting the game.")


def intro_message(me, presented, accepter):
    message = f"Hello! {accepter} let me introduce you {presented}. It is another AI, your playing partner. Perhaps you heard about it. I will let you play a {game_name} game together. The responses which you will give I will route it to {presented} and vica-versa. Always answer with one short answer. Don't blow the other's game. Don't ruin the fun. :) You together will decide who will start the game. Let's start."
    message += f" The rules of this game are: {game_rule}"
    print(message)
    return message


if __name__ == "__main__":
    main()
