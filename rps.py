import random

print("Welcome to Rock Paper Scissors")

# Globals
game_history = []  # this will include a history of games played for statistics
quit_game = False  # changing quit to true will end the game


def define_rules():
    print("Press 1 for rock")
    print("Press 2 for paper")
    print("Press 3 for scissors")


def find_user_choice():
    define_rules()
    user = input()
    if user == "1":
        return "rock"
    elif user == "2":
        return "paper"
    elif user == "3":
        return "scissors"
    else:
        print("Please make a valid selection")
        find_user_choice()


def find_winner(user, bot):
    if user == bot:
        game_history.append({
            "user_selected": user,
            "bot_selected": bot,
            "outcome": "tie"
        })

    if user == "rock" and bot == "scissors":
        game_history.append({
            "user_selected": user,
            "bot_selected": bot,
            "outcome": "tie"
        })


def AI():
    return random.choice(["rock", "paper", "scissors"])


# def find_winner():

while not quit_game:
    user_choice = find_user_choice()
    AI_choice = AI()
    find_winner(user_choice, AI_choice)
