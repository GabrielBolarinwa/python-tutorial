# ● ┌ ─ ┐ │ └ ┘

"┌─────────┐"
import random

"│         │"
"│    ●    │"
"│         │"
"└─────────┘"

dice_art = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"
    ),
    5: (
        "┌─────────┐",
        "│ ●     ● │",
        "│    ●    │",
        "│ ●     ● │",
        "└─────────┘"
    ),
    6: (
        "┌─────────┐",
        "│ ●  ●  ● │",
        "│         │",
        "│ ●  ●  ● │",
        "└─────────┘"
    ),
}

dice = []
total = 0

while True:
    num_of_dice = input("How many dice?: ")
    if num_of_dice.isdigit():
        num_of_dice = int(num_of_dice)
        for die in range(num_of_dice):
            dice.append(random.randint(1, 6))
        for line in range(5):
            for die in dice:
                print(dice_art.get(die)[line], end="")
            print()
        for die in dice:
            total += die
        print(f"Total: {total}")
        break
    else:
        print("Please enter a valid number")
