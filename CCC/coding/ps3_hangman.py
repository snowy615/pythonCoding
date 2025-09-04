# Hangman game
import random
WORDLIST_FILENAME = "words.txt"
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """

    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    ha = 0
    secretWord = list(secretWord)
    list(lettersGuessed)
    for z in range(len(secretWord)):
        if secretWord[z] not in lettersGuessed:
            ha = 1
            return False
    if ha == 0:
        return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    list(secretWord)
    list(lettersGuessed)
    word = list(secretWord)
    fword = ''
    for y in range(len(secretWord)):
        if secretWord[y] not in lettersGuessed:
            fword += '_'
        else:
            fword += secretWord[y]
    return fword

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
    for z in range(len(lettersGuessed)):
        if lettersGuessed[z] in alpha:
            alpha.pop(alpha.index(lettersGuessed[z]))
    word = ''
    for y in range(len(alpha)):
        word += alpha[y]
    return word

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game Hangduck!')
    print('I am thinking of a word that is %s letters long.' %(len(secretWord)))
    guess = 8
    ha = 0
    lettersGuessed = []
    while guess > 0:
        print('-----------')
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print('Congratulations, you won!')
            ha = 1
            break
        else:
            print('You have %s guesses left.' %guess)
            print('Available letters: ', end='')
            print(getAvailableLetters(lettersGuessed))
            letter = input('Please guess a letter: ')
            lettersGuessed.append(letter)
            if lettersGuessed.count(letter) > 1:
                print("Oops! You've already guessed that letter: ", end='')
                print(getGuessedWord(secretWord, lettersGuessed))
            elif letter in secretWord:
                print('Good guess: ', end='')
                print(getGuessedWord(secretWord, lettersGuessed))
            else:
                print('Oops! That letter is not in my word: ', end='')
                print(getGuessedWord(secretWord, lettersGuessed))
                guess -= 1
    if ha == 0:
        print('-----------')
        print('Sorry, you ran out of guesses. The word was %s.' %secretWord)


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
