import string

ASCII_LETTERS = string.ascii_lowercase


def LongestWord(str_):
    """Search the largest word in a string
    :param str_: string parameter which will contain any character
    """
    sentence = ''
    # Remove all characters that not belong to the ascii alphabet
    for item in str_:
        if item.lower() in ASCII_LETTERS or item == ' ':
            sentence += item

    # Sort words by length and return the last item
    sorted_words = sorted(sentence.split(' '), key=len)
    return sorted_words[-1]
