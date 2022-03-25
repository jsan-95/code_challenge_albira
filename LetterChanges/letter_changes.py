import string

ASCII_LETTERS = string.ascii_lowercase
VOWELS = ['a', 'e', 'i', 'o', 'u']


def LetterChanges(str_):
    """Replace every letter in the string with the letter following it in
    the alphabet
    :param str_: string parameter which will contain any character
    """
    res = ''

    for item in str_:
        if item not in ASCII_LETTERS:
            res += item
            continue

        index_alphabet = ASCII_LETTERS.index(item)
        index = index_alphabet + 1
        if index >= len(ASCII_LETTERS):
            index = 0

        letter = ASCII_LETTERS[index]
        if letter in VOWELS:
            letter = letter.upper()

        res += letter

    return res
