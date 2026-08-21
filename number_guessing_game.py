import random

low = 1
high = 100
guesses = 0
number = random.randint(low, high)
is_running = True

print("A random number has been selected between 1 and 100, can you guess it?")
while is_running:
    guess = input("Enter a guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess != number:
            if guess > high or guess < low:
                print("Please enter a number between 1 and 100")
            else:
                print("You guessed wrong")
                if guess > number:
                    print("The number is smaller, try again")
                else:
                    print("The number is bigger, try again")
        else:
            is_running = False
    else:
        print("Please enter a number")

print(f"Congratulations you have successfully the random number, it took you {guesses} guesses")
