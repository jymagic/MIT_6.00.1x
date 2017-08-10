def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.

    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    output = hand.copy()
    if word in wordList:
        for letter in word:
            if output.get(letter.lower(), 0) > 0:
                output[letter] = output.get(letter, 0) - 1
            else:
                return False
                break
        return True
    else:
        return False