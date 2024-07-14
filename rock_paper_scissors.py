import random

# Function to get the user's input
def get_users_input():
    user_input = input("Enter your choice (rock, paper, scissors): ").lower()

    # Checking if the input of the user is valid.
    while user_input not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose again.")
        user_input = input("Enter your choice (rock, paper, scissors): ").lower()
    return user_input

# Function to get the computer's input
def get_computers_input():
    choices = ["rock", "paper", "scissors"]
    computer_input = random.choice(choices)
    return computer_input

# Determining the winner of the game
def determine_winner(user_input, computer_input):
   
    if user_input == computer_input:
        return "It's a tie!"
    # Define the rules for winning
    elif (user_input == "rock" and computer_input == "scissors") or \
         (user_input == "paper" and computer_input == "rock") or \
         (user_input == "scissors" and computer_input == "paper"):
        return "You win!"
    else:
        return "You lose!"

# Function to run the game.
def main():
    print("Welcome to Rock, Paper, Scissors!")
    user_input = get_users_input()
    computer_input = get_computers_input()
    
    print(f"You chose: {user_input}")
    print(f"Computer chose: {computer_input}")
    
    # Displaying the result.
    result = determine_winner(user_input, computer_input)
    print(result)

# Running the game.
if __name__ == "__main__":
    main()