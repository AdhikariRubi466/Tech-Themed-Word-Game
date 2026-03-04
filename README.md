# Tech Word Guess Game

A Django-based word guessing game inspired by Wordle, where all words are related to technology.  
Players choose a difficulty level and try to guess the secret word within limited attempts.

---

## Features

- Tech-themed word guessing game
- Three difficulty levels (Easy, Medium, Hard)
- Word preview memory challenge
- Feedback system for guesses
- Score calculation
- Modern UI with glassmorphism design
- Background image support
- Django session-based game state

---

## How the Game Works

1. Player selects a difficulty level.
2. The game shows a list of possible words for a short time.
3. Player must memorize the words.
4. The player guesses the secret word.
5. Feedback is given for each letter:
   - Correct letter and position
   - Letter exists but wrong position
   - Letter not in the word
6. Player has **6 attempts** to guess correctly.

---

## Difficulty Levels

| Level | Multiplier | Word Difficulty |
|------|------------|----------------|
| Easy | 1x | Basic tech terms |
| Medium | 2x | Intermediate tech terms |
| Hard | 3x | Advanced tech terms |

Score is calculated based on remaining attempts and difficulty.

---

## Project Structure
