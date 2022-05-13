import random
top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("please type a number larger than 0")
        quit()
else:
    print("Type a number next time")
    quit()


r = random.randrange(top_of_range)
guesses = 0


while True:
    guesses += 1
    user_guess = input("make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("Type a number next time")
        continue

    if user_guess == r:
        print("You got it!")
        break
    else:
        if user_guess > r:
            print("You were above the number!")
        else:
            print("You were below the number!")

print("you got it in", guesses, "guesses")
