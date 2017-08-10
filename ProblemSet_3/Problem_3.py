def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    string = string.ascii_lowercase
    printout = ''
    for i in string:
        if i not in lettersGuessed:
            printout = printout + i
    return printout
