import os
import requests
# Fetch a random word from an API
def get_random_word():
    try:
        response = requests.get('https://random-word-api.vercel.app/api?words=1')
        if response.status_code == 200:
            word = response.json()[0]
            return word.lower()
        else:
            print("Failed to fetch a word from the API. Using default word 'python'.")
            return 'python'
    except Exception as e:
        print(f"Error fetching word: {e}. Using default word 'hangman'.")
        return 'hangman'
# Get the secret word from API
secret_word = get_random_word()
# Clear screen
os.system('cls' if os.name == 'nt' else 'clear')
guessedWord = ['_'] * len(secret_word)
attempts = 10
while attempts > 0:
    print('\nCurrent word: ' + ' '.join(guessedWord))
    guess = input('Guess a letter: ').lower()
    if guess in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessedWord[i] = guess
        print('Correct!')
    else:
        attempts -= 1
        print('Wrong guess! Attempts left: ' + str(attempts))
    if '_' not in guessedWord:
        print('\nCongratulations!! You have guessed the word: ' + secret_word)
        break
if attempts == 0 and '_' in guessedWord:
    print('\nYou\'ve run out of attempts! The word was: ' + secret_word)