def _get_index_of_numbers(str_):
    """Find the numbers in a string and fill an array with their index"""
    return [i for i, item in enumerate(str_) if item.isnumeric()]


def _count_question_marks(str_split):
    """Sum the occurrences of question marks in a string"""
    count = 0
    for item in str_split:
        if item == '?':
            count += 1

    return count


def QuestionsMarks(str_):
    """Check if there are exactly 4 question marks between every pair of two
    numbers that add up to 12

    :param str_: string parameter which will contain single digit numbers,
    letters, and question marks
    """

    if not str_:
        return False

    indexes = _get_index_of_numbers(str_)

    prev = indexes[0]
    for index in indexes[1:]:
        if index - prev < 5 or int(str_[prev]) + int(str_[index]) != 12:
            prev = index
            continue

        count = _count_question_marks(str_[prev + 1:index])

        if count == 4:
            return True

    return False
