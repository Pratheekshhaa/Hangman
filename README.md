
# Hangman


Hangman - One Player Game with Random Word API

This is a simple command-line implementation of the classic **Hangman** game in Python. The twist? It uses a **Random Word API** to fetch a new secret word every time, so it's a fully automated one-player experience.

### 💡 Features

- Fetches a random word using a public API
- One-player mode – no need for someone to enter the word manually
- 10 attempts to guess the word
- Easy to customize and extend

### 📦 Requirements

- Python 3.x
- `requests` library

   Install the required package with:
   ```
         `pip install requests`
   ```

### 🧠 How to Play

1. Run the script:

   ```bash
   python hangman.py
   ```
2. The script will automatically fetch a random secret word.
3. Start guessing one letter at a time.
4. You have 10 incorrect guesses before the game ends.

### 🔗 Random Word API

This project uses [https://random-word-api.vercel.app/api?words](https://random-word-api.vercel.app/api?words) to fetch words.

### 🛠️ Future Improvements

- Add difficulty levels (easy/medium/hard)
- Support phrases or multi-word challenges
- Add a graphical or web interface
- Allow to choose categories 



Feel free to fork, modify, and contribute!



