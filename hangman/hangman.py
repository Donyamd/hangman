import random
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''']
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()
# print(words)

def displayboard(missedLetters, correctLetters, secretWord) :
    print(HANGMAN_PICS[len(missedLetters)])
    print()
    print("missedLetters:", end=" ")
    for letter in missedLetters:
        print(letter, end= " ")
    print()

    blanks = "_" * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
    for letter in blanks:
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
        while True:
            print("Guess a letter:")
            guess = input()
            guess = guess.lower()
            if len(guess) != 1:
                print("please enter a single LETTER.")
            elif guess in alreadyGuessed:
                print("you have already guessed that letter. choose again.")
            else:
                return guess


def playAgain():
    print("do you wanna play again ?(yes or no)")
    return input().lower().startswith("y")

print("HANGMAN")
missedLetters = " "
correctLetters = " "
secretWord = random.choice(words)
gameIsDone = False

while True :
    displayboard(missedLetters, correctLetters , secretWord)
    guess = getGuess(missedLetters + correctLetters)
    if guess in secretWord:
        correctLetters = correctLetters + guess
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
            break
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Check if player has guessed too many times and lost.
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayboard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' +str(len(missedLetters)) + ' missed guesses and ' +str(len(correctLetters)) + ' correct guesses,the word was "' + secretWord + '"')
            gameIsDone = True

    # Ask the player if they want to play again (but only if the game is done).
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = random.choice(words)
        else:
            break



