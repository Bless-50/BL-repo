
# File: rps.py
# Description: <Rock-Paper-Scissors Game>
# Assignment Number: 7
# Name: <BLESSING LARBI>
# SID:  <2425404881>
# Email: <242544881@live.gctu.edu.gh>
# Grader: <Augustus Buckman>
# On my honor, <Blessing Larbi>, this programming assignment is my own work
# and I have not provided this code to any other student.


import random

def get_computer_choice():
    """Return computer's choice as a string."""
    num = random.randint(1, 3)
    if num == 1:
        return "Rock"
    elif num == 2:
        return "Paper"
    else:
        return "Scissors"


def get_player_choice():
    """Prompt player for choice and validate input."""
    print("Enter your choice (Rock, Paper, Scissors): ", end="")
    choice = input().strip().capitalize()
    while choice not in ("Rock", "Paper", "Scissors"):
        print("Invalid choice. Try again: ", end="")
        choice = input().strip().capitalize()
    return choice


def determine_winner(player, computer):
    """Determine winner and return result string."""
    if player == computer:
        return "Tie"
    elif (player == "Rock" and computer == "Scissors") or \
         (player == "Paper" and computer == "Rock") or \
         (player == "Scissors" and computer == "Paper"):
        return "Player"
    else:
        return "Computer"


def play_round():
    """Play one round and display results."""
    player = get_player_choice()
    computer = get_computer_choice()
    print(f"Computer chose: {computer}")
    winner = determine_winner(player, computer)
    if winner == "Tie":
        print("It's a tie!")
    elif winner == "Player":
        print("You win!")
    else:
        print("Computer wins!")
    return winner


def main():
    """Main function controlling game flow."""
    print("Do you want to set the seed? (1 for yes, 0 for no): ", end="")
    seed_choice = input().strip()
    if seed_choice == "1":
        print("Enter seed: ", end="")
        seed_value = int(input().strip())
        random.seed(seed_value)

    print("How many rounds do you want to play? ", end="")
    rounds = int(input().strip())
    if rounds <= 0:
        print("Invalid number of rounds.")
        return

    player_wins = 0
    computer_wins = 0
    ties = 0

    for _ in range(rounds):
        result = play_round()
        if result == "Player":
            player_wins += 1
        elif result == "Computer":
            computer_wins += 1
        else:
            ties += 1

    print("\nGame Over!")
    print(f"Player wins: {player_wins}")
    print(f"Computer wins: {computer_wins}")
    print(f"Ties: {ties}")

if __name__ == "__main__":
    main()
1