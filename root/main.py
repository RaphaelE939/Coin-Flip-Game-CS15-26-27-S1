import random

while True:
    coin = random.choice(["Heads", "Tails"])

    while True:
        guess = input("Heads or Tails?").lower().strip()
        if guess == "heads" or guess == "tails":
            break
        else:
            print("Invalid input.")


    if guess == coin:
        print("Correct!")
    else:
        print (f"Incorrect, the coin landed on {coin}")