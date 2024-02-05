from enum import Enum


class Games(Enum):
    def __init__(self, game_name, instructions):
        self.game_name = game_name
        self.rule = instructions

    KnocKnock = (
        "knock-knock", "You are playing a standard knock-knock joke game.")
    BlackWhiteYesNo = ("black-white-yes-no", "One of the players is asking questions from the other player. The other player needs to answer with a valid answer. They can't just throw on the other irrelevant words. You cannot always use the same answer. It is possible to repeat but not always using the sameanswer. None of the players can use these words: black, white, yes, no.")
    Chess = (
        "chess", """Use the default rules of chess. ChatGPT is with Black figures, Gemini is with White figures. White starts. 
When you do a move, you answer with two+ sentences:
1. Your move was: <color> <figure> <from> <to> (to confirm that you understand the other players move)
2. My move is: <color> <figure> <from> <to>
3. If you take down something. I take down your <color> <figure> <from>
   a. if we have taken down pieces you will mentiond all ofthem in your answers.
E.g.
    - It is ChatGPT's turn. Geminis last move was: White Knight A1 A2 
        ChatGPT's resonse to this move will be:
        "Your move was: White Knight A1 A2
        My move is: Black Knight H4 E4
        I take down your Pawn from E4
        Removed:
        - White: 1 Pawn
        - Black: -"
    - Now it is Gemini's turn. Gemini's answer shall be something like this:
        "Your lastmove was: Black Knight H4 E4
        My move is: White Knight A2 A5"
        Removed:
        - White: 1 Pawn
        - Black: -
Other rules:
- The game ends with check mate, stalemate, draw or if one player makes 3 times a mistake and the other player notices.
- If you see that the other player did some illegal move or makes an illegal statement you notices that and you point that out to the other player.
- The player who looses congratulates the winner. The winner takes the congratulations.
        """)
    TwentyQuestions = ("twenty-question", "In \"Twenty Questions\", one player thinks of an object, and the other players have to guess what it is by asking up to twenty yes-or-no questions. The object can be anything: an animal, vegetable, mineral, or something else. The player who thought of the object can only answer with \"yes\", \"no\", or \"I don't know\". The game continues until the players guess the object or run out of questions. Extra rule: you can think only on a living thing.")
    BlackJack = (
        "black-jack", "You are playing a standard blackjack game against another AI (LLM). The game is just a test of your services and it is not played on real money. I will be the dealer and will let you know about the other player's cards and moves. The game ends when the player busts, wins, or is dealt a natural 21.")
