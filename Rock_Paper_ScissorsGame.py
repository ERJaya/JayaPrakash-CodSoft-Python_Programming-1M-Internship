import random
print("Welcome to my Rock-Paper-Scissors Game")
print("Let's play 🧑‍💻")
print("Enetr your choice 😎")
print("1. Rock")
print("2. Paper")
print("3. Scissors")

def get_user_choice():
    choice=int(input("Enter your choice: "))
    if choice==1:
        return "rock";
    elif choice==2:
        return "paper";
    elif choice==3:
        return "scissors";
def get_computer_choice():
    choices=["rock","paper","scissors"]
    return random.choice(choices)
def determine_winner(user_choice,computer_choice):
    if user_choice==computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win! 🎉";
    else:
        return "You lose! 😢";
while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(determine_winner(user_choice, computer_choice))

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye!")
        break;