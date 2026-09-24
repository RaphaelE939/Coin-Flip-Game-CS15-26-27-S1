import random
guess_score = 0

while True:
    choices = ["heads", "tails"]
    value = random.choice(["Heads", "Tails"])
    coin = random.choice(choices)
    while True:
        guess = input("\nMake a guess, Heads or Tails. "
                      
                      "\nIf you get it right, your incorrect guess score rests"
                      
                      "\nIf you get it wrong you gain 1 incorrect guess. "
                      
                      
                      "\nWhat is your choice? ")

        guess = guess.strip().lower()
        if guess == "heads" or guess == "tails":
            break
        else:
            print("Invalid input")


    if guess == coin:
        print("You are correct, hooray😁")
        guess_score -= guess_score
    else:
        guess_score += 1
        print("Incorrect, the coin landed on", coin.capitalize())
    if guess_score == 3:
        print("\nYou have made 3 incorrect guesss in a row. No more playtime.")
        break
    again = input("Do you want to play again? (yes/no): ").strip().lower()
    if again != "yes":
        print("Thanks for playing!")
        break