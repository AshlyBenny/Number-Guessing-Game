# 🎯 MindGuess — Number Guessing Game

A fun, interactive number guessing game built with HTML, CSS, and JavaScript — playable directly in the browser.

> **[▶ Play the Game](https://ashlybenny.github.io/MindGuess/)**

---

##  Game Modes

###  Player Guesses
The computer picks a secret number. Try to guess it before the timer runs out!
Hints like **Bigger ⬆** or **Smaller ⬇** guide you toward the answer.

### Computer Guesses
Think of any number — the computer uses a **binary search algorithm** to figure it out.
Tell it whether your number is Bigger, Smaller, or Correct.

---

##  Difficulty Levels

| Level  | Range  | Time Limit |
|--------|--------|------------|
| 🟢 Easy   | 1–50   | 50 seconds |
| 🟡 Medium | 1–100  | 70 seconds |
| 🔴 Hard   | 1–500  | 90 seconds |

---

##  Features

- Two game modes (Player Guesses / Computer Guesses)
- Difficulty selection with different ranges and timers
- Live countdown timer with blinking warning at 10 seconds
- Guess history tracking
- 🎉 Confetti animation on win
- Responsive design (works on mobile and desktop)
- Keyboard support (Arrow keys to change value, Enter to submit)

---

##  Technologies Used

- HTML5
- CSS3
- JavaScript (Vanilla)
- [canvas-confetti](https://github.com/catdad/canvas-confetti) library

---

##  Earlier Python Version

This project started as a **Python terminal game** before being converted into a web app.
The original Python version (`number_guessing_game.py`) is also included in this repository.

To run it locally:
```bash
python number_guessing_game.py
```

---

##  Project Structure

```
MindGuess/
├── index.html              # Main web game (HTML + CSS + JS)
├── number_guessing_game.py # Original Python terminal version
└── README.md
```

---

##  How It Works (Computer Mode)

The Computer Guesses mode uses **Binary Search**:
- Starts with the full range (e.g., 1–100)
- Always guesses the midpoint
- Narrows down based on your feedback
- Guaranteed to find any number in at most **log₂(range)** guesses

---

##  Author

**Ashly Benny** — [GitHub](https://github.com/AshlyBenny)
