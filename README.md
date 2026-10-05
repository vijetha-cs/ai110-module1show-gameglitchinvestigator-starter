# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable.

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: _"How do I keep a variable from resetting in Streamlit when I click a button?"_
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

I found bugs by playing the game and testing boundary inputs like 0, 100, and 99999. The game gave misleading hints and accepted values outside the expected range. I used AI to help locate the hint logic and refactor core functions into logic_utils.py, but I manually reviewed the changes and tested them before accepting them. I verified the fixes by running the Streamlit app and by adding pytest tests for hint direction, invalid text input, and difficulty range behavior.

## 📸 Demo Walkthrough

1. User opens the Glitchy Guesser game.
2. User selects Normal difficulty, which uses a guessing range of 1 to 100.
3. User enters 0, and the game shows an error because the guess is outside the valid range.
4. User enters 99999, and the game shows an error because the guess is outside the valid range.
5. User enters a valid guess below the secret number, and the game says to go higher.
6. User enters a valid guess above the secret number, and the game says to go lower.
7. User eventually guesses the correct number, and the game shows the win message and final score.

## 🧪 Test Results

txt
platform win32 -- Python 3.14.5, pytest-9.1.1, pluggy-1.6.0
collected 4 items

tests\test_game_logic.py ....

## 🚀 Stretch Features

I did not complete any optional stretch features for this submission.
