from engines.chatgpt import ChatGPT
from engines.gemini import Gemini
from games import Games
import keys.chatgpt_api as chatgpt_secret
import keys.gemini_api as gemini_secret
import random
from typing import List

WAIT_TIME = 2

game = Games.BlackJack
game_name = game.game_name
game_rule = game.rule

chatgpt_client = ChatGPT(game_name, chatgpt_secret.key, WAIT_TIME)
gemini_client = Gemini(
    game_name, gemini_secret.project_id, gemini_secret.key_location, WAIT_TIME)


def main():
    print(f"Welcome to the {game_name} game!")
    welcome_chatgpt = intro_message("John", "Gemini", "ChatGPT")
    chatgpt_client.message(welcome_chatgpt)
    welcome_gemini = intro_message("John", "ChatGPT", "Gemini")
    gemini_client.message(welcome_gemini)
    dealer_first_message = f"Dealer: Welcome Gemini! Let's start the game. I will flip the coin. Gemini, heads or tails?"
    print(dealer_first_message)
    gemini_coin_side = gemini_client.message(dealer_first_message)
    dealer_second_message = f"Dealer: Welcome ChatGPT! Let's start the game. I will flip the coin. I have let Gemini to choose the side. It's selection was: \n {gemini_coin_side}"
    print(dealer_second_message)
    chatgpt_client.message(dealer_second_message)
    flip_result = flip_a_coin()
    dealer_coin_flip_message = f"Dealer: I have flipped a coin and the result is {flip_result}"
    print(dealer_coin_flip_message)
    chatgpt_client.message(dealer_coin_flip_message)
    gemini_client.message(dealer_coin_flip_message)
    print(">>>>" + flip_result.lower())
    print(">>>>" + gemini_coin_side.lower())
    if flip_result.lower() in gemini_coin_side.lower():
        first_player_client = gemini_client
        first_player_name = "Gemini"
        second_player_client = chatgpt_client
        second_player_name = "ChatGPT"
    else:
        first_player_client = chatgpt_client
        first_player_name = "ChatGPT"
        second_player_client = gemini_client
        second_player_name = "Gemini"
    print("Dealer: ")
    print(f"First player: {first_player_name}, ")
    print(f"Second player: {second_player_name}")
    dealer_message = f"""Dealer: Let's start the game. I'll deal two cards to each player and one face-up and one face-down card to myself as the dealer. I will use an input like this:
        {first_player_name}'s hand: [Card 1], [Card 2]
        

        {second_player_name}'s hand: [Card 3], [Card 4]

        Dealer's hand: [Face-up Card], [Face-down Card]

        Here are the dealt cards:
    """
    print("Init deal >>")
    while True:
        dealer_input = input()
        if dealer_input.lower() == "next":
            break
        elif dealer_input.lower() == "exit":
            exit()
        dealer_message += dealer_input
    round = 1
    print()
    first_player_client.message(dealer_message)
    try:
        while True:
            try:
                while True:
                    if round == 1:
                        player_name = first_player_name
                        player_client = first_player_client
                    elif round == 2:
                        player_name = second_player_name
                        player_client = second_player_client
                    else:
                        break
                    dealer_message = f"{player_name}, \"Hit\" or \"Stand\"?"
                    print(f"Dealer: {dealer_message}")
                    response = player_client.message(dealer_message)
                    if "hit" in response.lower():
                        dealer_message = f"{player_name}'s hand after hitting: "
                        print(f"Dealer: {dealer_message}")
                        while True:
                            dealer_input = input()
                            if dealer_input.lower() == "next":
                                break
                            elif dealer_input.lower() == "exit":
                                exit()
                            dealer_message += dealer_input
                    elif "stand" in response.lower():
                        dealer_message = f"{player_name}'s hand after standing: "
                        print(f"Dealer: {dealer_message}")
                        while True:
                            dealer_input = input()
                            if dealer_input.lower() == "next":
                                break
                            elif dealer_input.lower() == "exit":
                                exit()
                            dealer_message += dealer_input
                        break
                    else:
                        dealer_message = f"{player_name} please repeate your statement."
                        print(f"Dealer: {dealer_message}")
                        continue
                    player_client.message(dealer_message)
            except KeyboardInterrupt:
                print()
                go_further = False
                while not go_further:
                    shall_we_go_further = input("Continue(y/n): ")
                    if shall_we_go_further.lower() == "n":
                        exit()
                    elif shall_we_go_further.lower() == "y":
                        break
            round += 1
            if round == 3:
                break
    except KeyboardInterrupt:
        print("Exiting the game.")
        exit()
    dealers_deal = input("My turn as the dealer: ")
    print(dealers_deal)
    first_player_client.message(dealers_deal)
    second_player_client.message(dealers_deal)
    print("Exiting the game.")


def dealer_message(dealer_cards: List[str], first_player_cards: List[str], second_player_cards: List[str], first_player_name, second_player_name):
    return f"""
        {first_player_name}'s hand: {first_player_cards}
    
        {second_player_name}'s hand: {second_player_cards}

        Dealer's hand: {dealer_cards}
    """


def intro_message(me, presented, accepter):
    message = f"Hello! {accepter} let me introduce you {presented}. It is another AI, your playing partner. Perhaps you heard about it. I will let you play a {game_name} game together. The responses which you will give I will route it to {presented} and vica-versa. Always answer with one short answer. Don't blow the other's game. Keep yourself to the rules. You can mention if you see that the other player brakes the rules. Don't ruin the fun. :) Dealer will flip a coin and will decide who will be the first player. Let's start."
    message += f" The rules of this game are: {game_rule}"
    print(message)
    return message


def flip_a_coin():
    return "Heads" if random.randint(0, 1) == 0 else "Tails"


if __name__ == "__main__":
    main()
