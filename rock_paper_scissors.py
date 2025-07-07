import random

print("Welcome to Rock-Paper-Scissors Game!")
print("Type 'rock', 'paper', or 'scissors' to play.\n")

user_score = 0
computer_score = 0

while True:
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()

    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid input! Please try again.")
        continue

    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)

    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    print("Score -> You:", user_score, "| Computer:", computer_score)

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Final Score - You:", user_score, "| Computer:", computer_score)
        print("Thanks for playing!")
        break
