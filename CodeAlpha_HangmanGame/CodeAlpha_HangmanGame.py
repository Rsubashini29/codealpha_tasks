import random

# Predefined list of 5 words
words = ["python", "university", "code", "alpha", "programming"]

# Select a random word
word = random.choice(words)
guessed = ["_"] * len(word)
incorrect_guesses = 0
max_incorrect = 6
guessed_letters = set()

print("Welcome to Hangman! Guess the word one letter at a time.")

while incorrect_guesses < max_incorrect and "_" in guessed:
    print(" ".join(guessed))
    print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}")
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.add(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print("Good guess!")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")

if "_" not in guessed:
    print(f"You win! The word was: {word}")
else:
    print(f"You lose! The word was: {word}")