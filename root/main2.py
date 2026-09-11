import random
score = 0

while True:
    choices = ["heads", "tails"]
    value = random.choice(["Heads", "Tails"])
    coin = random.choice(choices)
    while True:
        guess = input("Make a guess, Heads or Tails. "
                      
                      "If you get it wrong, you lose 1 point or don't gain points. "
                      
                      "If you get it right, you gain 1 point."
                      
                      " What is your choice? ")

        guess = guess.strip().lower()
        if guess == "heads" or guess == "tails":
            break
        else:
            print("Invalid input")


    if guess == coin:
        score += 1
        print("You are correct, hooray😁")
        print("Your score has increased by 1")
    else:
        score -= 1
        if score < 0:
            score = 0
        # if the score is less than 0, then set it back to 0
        print("Incorrect, the coin landed on", coin.capitalize())

        print(f" Your score is = {score}")
    again = input("Do you want to play again? (yes/no): ").strip().lower()
    if again != "yes":
        print("Thanks for playing!")
        print(score)
        break