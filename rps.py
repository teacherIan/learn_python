import random

# A basic implementation of RPS
print("Welcome to Rock Paper Scissors")

# Globals
game_history = []  # this will include a history of games played for statistics
quit_game = False  # changing quit to true will end the game


def define_rules():
    print("Press 1 for rock")
    print("Press 2 for paper")
    print("Press 3 for scissors")
    print("Press 4 to quit")


def find_user_choice():
    global quit_game

    define_rules()
    user = input()
    if user == "4":
        quit_game = True
        return

    if user == "1":
        return "rock"
    elif user == "2":
        return "paper"
    elif user == "3":
        return "scissors"
    else:
        print("Please make a valid selection")
        find_user_choice()


def view_statistics():
    games_won = 0
    games_lost = 0
    win_percentage = 0

    for i in range(len(game_history)):
        if game_history[i]['outcome'] == 'win':
            games_won = games_won + 1
        if game_history[i]['outcome'] == 'lose':
            games_lost = games_lost + 1

        win_percentage = games_won / len(game_history)

        if games_won == 0:
            print("Your winning percentage is: 0")
        else:
            print(f"Your winning percentage is: {win_percentage}")
            print(f"You have lost {games_lost} games, and won {games_won} games")

    print(f"You have played {len(game_history)} games  ")


def find_winner(user, bot):
    global game_history
    print(f"You picked {user} and the computer picked {bot}")
    if user == bot:
        game_history.append({
            "user_selected": user,
            "bot_selected": bot,
            "outcome": "tie"
        })
        print("Tie")

    elif user == 'rock':
        if bot == 'paper':
            game_history.append({
                "user_selected": user,
                "bot_selected": bot,
                "outcome": "lose"
            })
            print("You lose")
        else:
            print("You win")
            game_history.append({
                "user_selected": user,
                "bot_selected": bot,
                "outcome": "win"
            })

    elif user == 'paper':
        if bot == 'scissors':
            print("You lose")
            game_history.append({
                "user_selected": user,
                "bot_selected": bot,
                "outcome": "lose"
            })
        else:
            game_history.append({
                "user_selected": user,
                "bot_selected": bot,
                "outcome": "win"
            })
            print("You win")

    elif user == 'scissors':
        if bot == 'rock':
            game_history.append({
                "user_selected": user,
                "bot_selected": bot,
                "outcome": "lose"
            })
            print("You lose")
        else:
            game_history.append({
                "user_selected": user,
                "bot_selected": bot,
                "outcome": "win"
            })
            print("You Win")

    view_statistics()

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
