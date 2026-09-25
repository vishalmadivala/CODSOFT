"""
Rock-Paper-Scissors Game
CodSoft Python Programming Internship - Task 4

A simple command-line Rock-Paper-Scissors game against the computer.
Tracks the score across multiple rounds and lets the user play again.
"""

import random

CHOICES = ["rock", "paper", "scissors"]
BEATS = {
    "rock": "scissors",
    "scissors": "paper",
    "paper": "rock",
}


def get_user_choice():
    while True:
        choice = input("Choose rock, paper, or scissors: ").strip().lower()
        if choice in CHOICES:
            return choice
        # Allow shorthand r/p/s
        shorthand = {"r": "rock", "p": "paper", "s": "scissors"}
        if choice in shorthand:
            return shorthand[choice]
        print("Invalid choice. Please type rock, paper, or scissors.")


def get_computer_choice():
    return random.choice(CHOICES)


def determine_winner(user, computer):
    if user == computer:
        return "tie"
    if BEATS[user] == computer:
        return "user"
    return "computer"


def play_round(score):
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"\nYou chose:      {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print("You win this round!")
        score["user"] += 1
    else:
        print("Computer wins this round!")
        score["computer"] += 1

    return score


def main():
    print("=" * 40)
    print("ROCK - PAPER - SCISSORS".center(40))
    print("=" * 40)

    score = {"user": 0, "computer": 0}

    while True:
        score = play_round(score)
        print(f"\nScore -> You: {score['user']}  |  Computer: {score['computer']}")

        again = input("\nPlay another round? (y/n): ").strip().lower()
        if again != "y":
            print("\nFinal Score:")
            print(f"  You: {score['user']}  |  Computer: {score['computer']}")
            if score["user"] > score["computer"]:
                print("Congratulations, you won overall! 🎉")
            elif score["user"] < score["computer"]:
                print("Computer won overall. Better luck next time!")
            else:
                print("Overall result: a tie!")
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
