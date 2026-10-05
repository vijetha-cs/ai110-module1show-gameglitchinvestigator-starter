# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
| ----- | ----------------- | --------------- | ---------------------- |
|       |                   |                 |                        |
|       |                   |                 |                        |
|       |                   |                 |                        |

### Bug 1: High boundary bug

What I did:
I guessed 90, 97, 99, 100, and even 99999.

What happened:
The game still said "Go higher," even for very high guesses.

What I expected:
The game should only accept guesses in the valid range, likely 1–100. If the user enters a number outside that range, the game should reject it instead of giving a hint.

### Bug 2: New Game button does not reset

What I did:
I clicked the "New Game" button after playing.

What happened:
The button seemed like it did not restart or reset the game clearly.

What I expected:
Clicking "New Game" should start a fresh game, reset the secret number, clear old guesses/messages, and reset the game state.

### Bug 3: Low boundary bug

What I did:
I entered 0 as a guess.

What happened:
The game accepted 0 and said "Go lower."

What I expected:
The game should reject 0 because it is outside the valid guessing range.

### Non-bug observation

I tested invalid text/symbol inputs like abc, &, and {.
The game did not accept them, so text validation seems to work correctly.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
