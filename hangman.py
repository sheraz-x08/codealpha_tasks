import random

words = ["python", "internship", "computer", "coding", "developer"]

def play():
    word = random.choice(words)
    guessed = []
    wrong = 0
    max_wrong = 6

    print("=== HANGMAN ===")
    while wrong < max_wrong:
        display = " ".join(c if c in guessed else "_" for c in word)
        print("\nWord:", display)
        print("Wrong guesses left:", max_wrong - wrong)

        if "_" not in display:
            print("You won! The word was:", word)
            return

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Enter a single letter only.")
        elif guess in guessed:
            print("You already guessed that.")
        else:
            guessed.append(guess)
            if guess in word:
                print("Correct!")
            else:
                wrong += 1
                print("Wrong!")

    print("Game over! The word was:", word)

play()
