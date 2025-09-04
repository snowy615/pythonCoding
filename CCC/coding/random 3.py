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
            # print(False)
            return False
    if ha == 0:
        # print(True)
        return True

# isWordGuessed('apple', ['e', 'i', 'k', 'p', 'r', 's'])

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
    for y in range(len(secretWord)):
        if secretWord[y] not in lettersGuessed:
            word[y] = '_ '
    for z in range(len(word)):
        print(word[z], end='')
getGuessedWord('apple', ['e', 'i', 'k', 'p', 'r', 's'])

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for z in range(len(lettersGuessed)):
        alpha.pop(alpha.index(lettersGuessed[z]))
    for y in range(len(alpha)):
        print(alpha[y], end='')
# getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's'])



