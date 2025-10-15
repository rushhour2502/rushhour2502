import random 


def hangman():
    word = random.choice(['man', "boy", "chair", "dog", "giraffe", "bananas", "sweater", "pumpkin", "elephant", "journey", "tornado", "library", "butterfly", "diamond"])
    valid_inputs = "abcdefghijklmnopqrstuvwxyz"
    turns = 10
    guess_made = ''

    while len(word) > 0:
        main = ''
        missed = 0

        for letter in word:
            if letter in guess_made:
                main += letter
                missed += 1
            else:
                main += "_" + ' '
        if main == word:
            print(word)
            print("You win!")
            break

        print("Guess the word ", main)
        guess = input()

        if guess in valid_inputs:
            guess_made += guess
        else:
            print("Enter a valid character")
            guess = input()

        if guess not in word:
            print(f"You have {turns} tries left")
            print("----------------------------")
            turns -= 1
            if turns == 1:
                print("last try, think carefully")
            if turns == 0:
                print("You loose")
                print("You let a kind man die")
                break


name = input("Enter your name: ")
print("Welcome ", name)
print("Try to guess the right word in less than 10 attempts")
print("---------------")
hangman()
