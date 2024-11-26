import random

def play_game():
    you_score = 0
    computer_score = 0

    while True:
        computer = random.choice([1, 2, 3])
        youstr = input("Enter Your Choice (R for Rock, P for Paper, S for Scissor): ").upper()
        youdict = {'R': 1, 'P': 2, "S": 3}
        revdict = {1: "Rock", 2: "Paper", 3: "Scissor"}

        if youstr not in youdict:
            print("Invalid input. Please choose R, P, or S.")
            continue

        you = youdict[youstr]

        print(f"You chose {revdict[you]} \nComputer chose {revdict[computer]}")

        if computer == you:
            print("It's a Draw!")
        elif (computer == 1 and you == 2) or (computer == 2 and you == 3) or (computer == 3 and you == 1):
            print("You Win!")
            you_score += 1
        else:
            print("You Lose!")
            computer_score += 1

        print(f"Scores - You: {you_score}, Computer: {computer_score}")

        play_again = input("Do you want to play again? (Y/N): ").upper()
        if play_again != 'Y':
            print(f"Final Scores - You: {you_score}, Computer: {computer_score}")
            if you_score > computer_score:
                print("Congratulations! You are the overall winner! 🎉")
            elif you_score < computer_score:
                print("Computer wins the game! Better luck next time! 🤖")
            else:
                print("It's a tie overall! Well played! 🤝")
            print("Thanks for playing!")
            break

# Start the game
play_game()
