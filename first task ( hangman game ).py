import random

# List of words
words = ["python", "computer", "student", "coding", "college"]

# Select random word
word = random.choice(words)

guessed_letters = []
attempts = 6

print("===== HANGMAN GAME =====")

while attempts > 0:

    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check win condition
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct Guess!")
    else:
        attempts -= 1
        print("❌ Wrong Guess!")
        print("Remaining Attempts:", attempts)

if attempts == 0:
    print("\n💀 Game Over!")
    print("The word was:", word)
