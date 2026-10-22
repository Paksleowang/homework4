import random
print("Welcome to Rock, Paper, Scissors: The Game")
user = 0
com = 0
rounds = 0
ties = 0

while True:
    question = input("Enter your choice: Rock, Paper, Scissor or q for quit: ").lower()

    if question == "q":
        print("\nThank you for playing.")
        print(f"You won {user}, the computer won {com}, draws: {ties}, Total rounds: {rounds}")
        break

    if question not in ["rock", "paper", "scissor"]:
        print("Invalid choices do not count as rounds.\n")
        continue

    computer = random.choice(["rock", "paper", "scissor"])
    print(f"Computer chose: {computer}")

    if question == computer:
        print("Draw!\n")
        rounds += 1
        ties += 1
        print(f"Round {rounds}: Draw\n")
    elif (question == "rock" and computer == "scissor") or \
         (question == "paper" and computer == "rock") or \
         (question == "scissor" and computer == "paper"):
        rounds += 1
        user += 1
        print("You win!\n")
        print(f"Round {rounds}: You win.\n")
    else:
        rounds += 1
        com += 1
        print("You lose!\n")
        print(f"Round {rounds}: You lose.\n")