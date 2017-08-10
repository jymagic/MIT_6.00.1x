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
    # FILL IN YOUR CODE HERE...
    lettersGuessed = []
    print('Welcome to the game, Hangman!' + '\n' \
          + 'I am thinking of a word that is %d letters long' % len(secretWord))
    print('------------')

    i = 8
    while i > 0:
        while True:
            print('You have %d guesses left.' % i + '\n' \
                  + 'Available Letters: %s' % getAvailableLetters(lettersGuessed))
            guess = str(input('Please guess a letter: ')).lower()
            if guess.isalpha() == False or len(guess) != 1:
                print('Please enter a letter ONLY')
                print('------------')
            elif guess not in getAvailableLetters(lettersGuessed):
                print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
                print('------------')
            else:
                break
        lettersGuessed.append(guess)

        if guess in secretWord:
            print('Good guess: '+ getGuessedWord(secretWord, lettersGuessed))
            print('------------')
            i += 1
        else:
            print('Oops! That letter is not in my word: '+ getGuessedWord(secretWord, lettersGuessed))
            print('------------')

        if isWordGuessed(secretWord, lettersGuessed) == True:
            print('Congratulations, you won!')
            exit()

        i -= 1
    print('Sorry, you ran out of guesses. The word was else. ')