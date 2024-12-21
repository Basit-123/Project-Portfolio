import random

# List of words for the game
words = ["apple", "banana", "grape", "orange", "mango"]

# Choose a random word
word = random.choice(words)
guessed_word = ["_"] * len(word)
attempts = 6
guessed_letters = []

print("Welcome to Hangman!")
print(" ".join(guessed_word))

while attempts > 0 and "_" in guessed_word:
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Enter a single valid letter!")
        continue

    if guess in guessed_letters:
        print(f"You already guessed '{guess}'.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        print("Good guess:", " ".join(guessed_word))
    else:
        attempts -= 1
        print(f"Wrong guess! You have {attempts} attempts left.")

if "_" not in guessed_word:
    print(f"Congratulations! You guessed the word: {word}")
else:
    print(f"Game over! The word was: {word}")
