import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock/paper/scissors) or 'exit' to quit: ").lower()
        if user_choice in ["rock", "paper", "scissors", "exit"]:
            return user_choice
        else:
            print("Invalid choice. Please choose from 'rock', 'paper', 'scissors', or 'exit'.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == "rock":
        return "You win!" if computer_choice == "scissors" else "Computer wins!"
    elif user_choice == "paper":
        return "You win!" if computer_choice == "rock" else "Computer wins!"
    elif user_choice == "scissors":
        return "You win!" if computer_choice == "paper" else "Computer wins!"

def play_game():
    while True:
        user_choice = get_user_choice()
        if user_choice == "exit":
            print("Thanks for playing. Goodbye!")
            break

        computer_choice = get_computer_choice()
        print(f"Computer chooses: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)
        print()

if __name__ == "__main__":
    print("Welcome to Rock Paper Scissors game!")
    play_game()
