import random


def user_input_validation(game_options):
    while True:
        user_input = input("\n> ").strip()
        options = ["!exit", "!rating"] + game_options

        if user_input in options:
            break  # The loop stops if the user has entered a valid value
        else:
            print("Invalid input!")  # The loop iterates until the user has entered a valid value

    return user_input


def random_computer_choice(game_options):
    random_number = random.randrange(len(game_options))
    computer_choice = game_options[random_number]

    return computer_choice


def match_decision(user_choice, computer_choice, game_options):
    game_status_choices = ["win", "loss", "draw"]
    game_status = ""
    index = 0

    # Finds position of user_choice in the game_options list
    for j in range(len(game_options)):
        if game_options[j] == user_choice:
            index = j
            break

    # Removes user_choice from game_options list
    # Then it rearranges the list to be able to identify which option beats which
    if index == 0:
        game_options = game_options[1:]
    elif index == (len(user_choice) - 1):
        game_options = game_options[:-1]
    else:
        game_options = game_options[index + 1:] + game_options[:index]

    # Divides the game_options to identify a user win or loss
    # A computer_choice that is in the left-hand side of the game_options list is a loss for the user
    # A computer_choice that is in the right-hand side of the game_options list is a win for the user
    user_win = game_options[(len(game_options) // 2):]
    user_loss = game_options[:(len(game_options) // 2)]

    if user_choice == computer_choice:
        game_status = game_status_choices[2]  # draw
    elif computer_choice in user_win:
        game_status = game_status_choices[0]  # win
    elif computer_choice in user_loss:
        game_status = game_status_choices[1]  # loss

    return game_status


def get_user_rating(user_name):
    file = open("rating.txt", "r")
    user_rating = "0"  # Gives the user a rating of 0 if their name is not in the file

    for line in file:
        line_contents = line.split(" ")  # User name and score is on same line and separated by a space character

        if line_contents[0] == user_name:
            user_rating = line_contents[1]
            break

    file.close()

    return user_rating


def update_user_rating(current_user_rating, game_status):
    if game_status == "win":
        new_rating = str(int(current_user_rating) + 100)
    elif game_status == "draw":
        new_rating = str(int(current_user_rating) + 50)
    else:
        new_rating = current_user_rating

    return new_rating


def output_match_results(game_status, computer_choice):
    if game_status == "draw":
        print(f"There is a draw ({computer_choice})")

    elif game_status == "win":
        print(f"Well done. The computer chose {computer_choice} and failed")

    elif game_status == "loss":
        print(f"Sorry, but the computer chose {computer_choice}")


def main_program():
    user_name = input("Enter your name: ")
    print(f"\nHello, {user_name}")

    user_rating = get_user_rating(user_name)
    game_options = input("\nEnter game options. (e.g. rock,paper,scissors) ").strip().split(",")  # User enters the game options and it gets split into a list

    # If the user enters nothing then game is played with basic game options
    if game_options[0] == "":
        game_options = ["rock", "paper", "scissors"]

    print("\nOkay, let's start")
    print("\nCommands: !exit and !rating")
    print("Enter your option")

    while True:
        user_input = user_input_validation(game_options)  # The user enters a choice to be validated

        if user_input == "!rating":
            print(f"Your rating: {user_rating}")
            continue
        if user_input == "!exit":
            print("Bye!")
            break

        computer_choice = random_computer_choice(game_options)

        match_result = match_decision(user_input, computer_choice, game_options)
        user_rating = update_user_rating(user_rating, match_result)
        output_match_results(match_result, computer_choice)


main_program()
