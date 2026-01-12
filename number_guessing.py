import random

print("Welcome!!")

def choose_levels():
    score = 0 
    levels = [
        {"level":1, "max": 10, "attempts":5},
        {"level":2, "max": 50, "attempts":6},
        {"level":3, "max": 100, "attempts":8},

    ]

    for l in levels:
        print(f"level- {l['level']}")
        print("RULES!!")
        print(f"Level {l['level']}")
        print(f"- You will have to guess number between 1 to {l['max']}")
        print(f"- You will have {l['attempts']} attempts")

        num = random.randint(1, l['max'])
        attempts = 0

        while attempts < l['attempts']:
            number_input = int(input("tell your guess: "))
            attempts += 1

            if number_input < num:
                print("The guess is too low.Try again.")
                print(f"You have {l['attempts']- attempts} guesses left.")

            elif number_input > num:
                print("the guess is too high ")
                print(f"you have {l['attempts']-attempts} guesses left")

    
            else:
                print("Congratulations!! the guess is correct!")
                break    
    

        if number_input != num:
            print(f"GAME OVER!!.The number was {num}")
             
        else:
            print(f"Level {l['level']} cleared! Moving to next level...")
            score += 10
            print(f"current score: {score}")


##replay option
while True:
    choose_levels()
    choice = input("Do you want to play again? (y/n): ").lower()
    if choice !='y':
        break
       