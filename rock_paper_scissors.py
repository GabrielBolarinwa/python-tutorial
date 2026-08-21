import random

options = ("rock", "paper", "scissors")

print("Rock, Paper, Scissors game")
user_score = 0
computer_score = 0
is_running = True

while is_running:
    user_choice = input("Please enter a choice i.e rock, paper or scissors (q for quit): ")
    if user_choice.lower() in options:
        computer_choice = random.choice(options)
        print(f"The computer chose {computer_choice}")
        if user_choice == computer_choice:
            print("TIE")
        elif user_choice == "rock" and computer_choice == "paper":
            print("Computer wins")
            computer_score += 1
            print(f"The score is You: {user_score} - Computer: {computer_score}")
        elif computer_choice == "rock" and user_choice == "paper":
            print("You win")
            user_score += 1
            print(f"The score is You: {user_score} - Computer: {computer_score}")
        elif computer_choice == "rock" and user_choice == "scissors":
            print("Computer wins")
            computer_score += 1
            print(f"The score is You: {user_score} - Computer: {computer_score}")
        elif computer_choice == "scissors" and user_choice == "rock":
            print("You win")
            user_score += 1
            print(f"The score is You: {user_score} - Computer: {computer_score}")
        elif computer_choice == "scissors" and user_choice == "paper":
            print("Computer wins")
            computer_score += 1
            print(f"The score is You: {user_score} - Computer: {computer_score}")
        elif user_choice == "paper" and computer_choice == "scissors":
            print("You win")
            user_score += 1
            print(f"The score is You: {user_score} - Computer: {computer_score}")
    elif user_choice == "q":
        print(f"The final score is You: {user_score} - Computer: {computer_score}")
        is_running = False
    else:
        print("Please enter a valid game option")
