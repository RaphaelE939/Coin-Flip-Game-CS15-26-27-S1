import random

while True:
    choices = ["heads", "tails"]
    value = random.choice(["Heads", "Tails"])
    coin = random.choice(choices)
    guess = input("What is your guess, Heads or Tails?\n")
    while guess not in ["heads", "tails"]:
       guess = guess.lower()

    if guess == coin:
        print("You are correct, hooray😁")
    else:

        print("Incorrect, the coin landed on", coin.capitalize())

    again = input("Do you want to play again? (yes/no): ").strip().lower()
    if again != "yes":
        print("Thanks for playing!")
        break