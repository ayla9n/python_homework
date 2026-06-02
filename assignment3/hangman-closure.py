#Task 4: Closure Practice

def make_hangman(secret_word):
    guesses = []
    def hangman_closure(letter):
        word = ""
        guesses.append(letter)
        for l in secret_word:
            if l in guesses:
                word += l
            else: 
                word += "_"
        print(word)
        return "_" not in word

    return hangman_closure


secret_word = input("Enter secret word: \n")
game = make_hangman(secret_word)

win = False

while not win:
    letter = input("Guess a letter: \n")
    win = game(letter)

print("you've guessed all the letters!")
