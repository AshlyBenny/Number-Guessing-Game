import random
import time
import threading

GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
RESET = "\033[0m"

# Shared flag to signal when time is up
time_up = False

def countdown_timer(time_limit):
    """Runs in background, prints remaining time every 10 seconds, sets time_up flag."""
    global time_up
    start = time.time()
    while True:
        elapsed = time.time() - start
        remaining = int(time_limit - elapsed)
        if remaining <= 0:
            time_up = True
            print(f"\n\n⏰ {RED}TIME'S UP! Game Over!{RESET}")
            print("(Press Enter to continue...)")
            break
        time.sleep(1)  # Check every second

while True:
    time_up = False

    print("""
╔════════════════════════════════════╗
       🎯 NUMBER GUESSING GAME
╚════════════════════════════════════╝
""")
    print(f"{YELLOW}Try to guess the secret number before time runs out! ⏳{RESET}")
    print(f"{YELLOW}Good luck \n{RESET}")
    print("Choose Difficulty Level")
    print("-----------------------")
    print(f"{GREEN}1. Easy (1-50, 50 seconds){RESET}")
    print(f"{YELLOW}2. Medium (1-100, 70 seconds){RESET}")
    print(f"{RED}3. Hard (1-500, 90 seconds){RESET}")
    print()

    while True:
        try:
            choice = int(input("Enter your choice (1/2/3): "))
            if choice in [1, 2, 3]:
                break
            else:
                print("⚠️  Please enter 1, 2, or 3.")
        except ValueError:
            print("⚠️  Please enter a valid number!")

    if choice == 1:
        number = random.randint(1, 50)
        max_range = 50
        time_limit = 50
        print(f"{GREEN}✔ Easy mode selected! Guess between 1 and 50.{RESET}\n")
    elif choice == 2:
        number = random.randint(1, 100)
        max_range = 100
        time_limit = 70
        print(f"{YELLOW}✔ Medium mode selected! Guess between 1 and 100.{RESET}\n")
    else:
        number = random.randint(1, 500)
        max_range = 500
        time_limit = 90
        print(f"{RED}✔ Hard mode selected! Guess between 1 and 500.{RESET}\n")

    print(f"⏰ You have {time_limit} seconds. Go!")
    print("----------------------------------\n")

    attempts = 0
    start_time = time.time()

    # FIX: Start timer in a background thread so it runs even during input()
    timer_thread = threading.Thread(target=countdown_timer, args=(time_limit,), daemon=True)
    timer_thread.start()

    while not time_up:
        remaining = int(time_limit - (time.time() - start_time))
        if remaining <= 0:
            break

        print(f"⏰ Time Left: {remaining}s")

        try:
            guess_str = input(f"Enter your guess (1 - {max_range}): ")
        except EOFError:
            break

        if time_up:
            break

        try:
            guess = int(guess_str)
        except ValueError:
            print("⚠️  Please enter a valid number!\n")
            continue

        if guess < 1 or guess > max_range:
            print(f"⚠️  Please enter a number between 1 and {max_range}\n")
            continue

        attempts += 1

        if guess == number:
            elapsed = time.time() - start_time
            print(f"\n{GREEN}==============================")
            print("🎉 Congratulations!")
            print(f"You guessed the number in {attempts} attempt(s)!")
            print(f"Time taken: {int(elapsed)} seconds")
            print(f"=============================={RESET}\n")
            break
        elif guess < number:
            print(f"{YELLOW}  ↑ Try bigger!{RESET}\n")
        else:
            print(f"{RED}  ↓ Try smaller!{RESET}\n")
    else:
        # Time ran out
        if not (time.time() - start_time < time_limit):
            print(f"\n{RED}The correct number was: {number}{RESET}")
            print("===================================\n")

    # Wait for timer thread to finish
    timer_thread.join(timeout=1)

    play_again = input("\nDo you want to play again? (y/n): ").strip().lower()
    if play_again != "y":
        print("👋 Thanks for playing! Goodbye!")
        break
    time_up = False

