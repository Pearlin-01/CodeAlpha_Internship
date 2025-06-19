import random

# Predefined word list
word_list = ["apple", "robot", "zebra", "pizza", "chair"]
chosen_word = random.choice(word_list)

# Game setup
guessed_word = ["_"] * len(chosen_word)
guessed_letters = []
attempts = 6

print("🎯 Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have", attempts, "wrong guesses allowed.\n")

while attempts > 0 and "_" in guessed_word:
    print("Word:", " ".join(guessed_word))
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❗ Please enter a single valid letter.\n")
        continue

    if guess in guessed_letters:
        print("🔁 You already guessed that letter!\n")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                guessed_word[i] = guess
        print("✅ Correct guess!\n")
    else:
        attempts -= 1
        print(f"❌ Wrong guess! {attempts} attempts left.\n")

# Final result
if "_" not in guessed_word:
    print("🎉 Congratulations! You guessed the word:", chosen_word)
else:
    print("💀 Game Over! The word was:", chosen_word)
