import random
import time

GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
RESET = "\033[0m"

while True:


 print("""
╔════════════════════════════════════╗
      🎯  NUMBER GUESSING GAME
╚════════════════════════════════════╝
""")
 print("\033[33mTry to guess the secret number before time runs out! ⏳\033[0m")
 print("\033[33mGood luck \n\033[0m")

 print("Choose Difficulty Level")
 print("-----------------------")
 print(f"{GREEN}1. Easy   (1-50){RESET}")
 print(f"{YELLOW}2. Medium (1-100){RESET}")
 print(f"{RED}3. Hard   (1-500){RESET}")
 print()

 while True:
    try:
        choice = int(input("Enter your choice: "))
        if choice in [1, 2, 3]:
            break
        else:
            print("⚠️ Please enter 1, 2, or 3.")
    except ValueError:
        print("⚠️ Please enter a valid number!")

 if choice == 1:
    number = random.randint(1, 50)
    max_range = 50
    time_limit = 50
    print("You chose Easy mode!")

 elif choice == 2:
    number = random.randint(1, 100)
    max_range = 100
    time_limit = 70
    print("You chose Medium mode!")

 else:
    number = random.randint(1, 500)
    max_range = 500
    time_limit = 90
    print("You chose Hard mode!")

 attempts = 0
 start_time = time.time()

 while True:
    current_time = time.time()
    remaining_time = int(time_limit - (current_time - start_time))

    if current_time - start_time > time_limit:
        print("\n===================================")
        print("⏰ Time's up! ❌ Game Over!")
        print(f"The correct number was : {number}")
        print("===================================")
        break

    print("\n----------------------------------")
    print(f"⏰ Time Left : {remaining_time} seconds")
    print("----------------------------------")

    try:
        guess = int(input(f"Enter your guess (1 - {max_range}) : "))
    except ValueError:
        print("⚠️ Please enter a valid number!")
        continue

    if guess < 1 or guess > max_range:
        print(f"⚠️ Please enter a number between 1 and {max_range}")
        continue

    attempts += 1

    if guess == number:
        print("\n\033[32m==============================")
        print("🎉 Congratulations!")
        print("You guessed the number correctly!")
        print(f"Total attempts: {attempts}")
        print("==============================\033[0m")
        break

    elif guess < number:
        print("\033[94m Try bigger ↑ \033[0m")

    else:
        print("\033[91m Try smaller ↓ \033[0m")

 play_again = input("\n Do you want to play again? (y/n): ").lower()

 if play_again != "y":
    print("👋 Thanks for playing!")
    break

