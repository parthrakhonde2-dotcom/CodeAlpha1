import random

# List of predefined words
words = ["python", "computer", "program", "hangman", "coding"]

# Select a random word
word = random.choice(words)

# Variables
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("=" * 40)
print("🎯 WELCOME TO HANGMAN GAME 🎯")
print("=" * 40)

while incorrect_guesses < max_attempts:

    # Display current progress
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\\nWord:", display_word)
    print(f"❤️ Attempts Left: {max_attempts - incorrect_guesses}")
    print("Guessed Letters:", " ".join(guessed_letters))

    # Check win condition
    if all(letter in guessed_letters for letter in word):
        print("\\n🎉 Congratulations! You guessed the word:", word)
        break

    # User input
    guess = input("\\nEnter a letter: ").lower()

    # Validation
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter only one alphabet letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check guess
    if guess in word:
        print("✅ Correct Guess!")
    else:
        incorrect_guesses += 1
        print("❌ Wrong Guess!")

# Lose condition
if incorrect_guesses == max_attempts:
    print("\\n💀 Game Over!")
    print("The correct word was:", word)

print("\\nThank you for playing! 😊")
