import random


def hangman():
    word = random.choice(['man', "boy", "chair", "dog", "giraffe", "bananas",
                          "sweater", "pumpkin", "elephant", "journey", "tornado",
                          "library", "butterfly", "diamond"])
    valid_inputs = "abcdefghijklmnopqrstuvwxyz"
    turns = 10
    guessed_letters = []
    current_guess = ['_'] * len(word)  # Track correct guesses

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters: {' '.join(current_guess)}")

    while turns > 0:
        guess = input("\nGuess a letter: ").lower().strip()

        # Validate input
        if len(guess) != 1:
            print("Please enter exactly one letter.")
            continue
        if guess not in valid_inputs:
            print("Please enter a valid letter (a-z).")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        # Check if letter is in word
        if guess in word:
            print(f"Correct! '{guess}' is in the word.")
            # Reveal all instances of the guessed letter
            for i, letter in enumerate(word):
                if letter == guess:
                    current_guess[i] = guess
        else:
            turns -= 1
            print(f"Wrong! '{guess}' is not in the word. You have {turns} turns left.")

        # Display current progress
        print(' '.join(current_guess))

        # Check for win
        if '_' not in current_guess:
            print(f"\nCongratulations! You guessed the word: {word}")
            continue

        if current_guess == word:
            input_again = input('Do you want to play again? (yes or no)>>> ').lower().strip()
            if input_again == 'yes':
                hangman()
            else:
                print('Thanks for playing!')
    print(f"\nGame over! The word was: {word}")


hangman()
