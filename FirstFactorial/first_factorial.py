def FirstFactorial(num_):
    """Compute the factorial of a number
    :param num_: Integer number
    """
    if num_ < 0:
        print('n must be > or = to 0')
        return False

    if num_ in [0, 1]:
        return 1
    else:
        return num_ * FirstFactorial(num_ - 1)
