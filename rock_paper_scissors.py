import random

users_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]

while True:
    users_input = input("Type Rock/Paper/Scissors or Q to quit : ").lower()
    if users_input == "q":
        break

    if users_input not in options:
        continue
    random_number = random.randint(0, 2)
    # rock:0 ,paper:1,scissors:2
    computer_pick = options[random_number]
    if users_input == "rock" and computer_pick == "scissors":
        print("You won ")
        users_wins += 1
    elif users_input == "scissors" and computer_pick == "paper":
        print("You won!")
        users_wins += 1
    elif users_input == "paper" and computer_pick == "rock":
        print("You won!")
        users_wins += 1
    else:
        print("You lost")
        computer_wins += 1

print(
    f"You win {users_wins} times and losed against the computer {computer_wins} times. "
)
print("Goodbye!")
