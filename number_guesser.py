import random
import keyboard


while True:
    stop_range = input("Type a number to stop range of randomizer: ")

    if stop_range.isdigit():
        stop_range = int (stop_range)

        if stop_range <= 0:
            print("Please type a larger number next time.")
            continue
    else:
        print("Please type a number next time.")
        continue

    random_number = random.randrange(stop_range);

    user_guess = input("What number you think are guessed: ");
    if not user_guess.isdigit():
        print("Please type a number next time.")
        continue
    else:
        user_guess = int(user_guess)

    if user_guess == random_number:
        print("Congratulations: You win!")
    else:
        print(f"You got it wrong. Guessed number was {random_number}. Try better next time")
