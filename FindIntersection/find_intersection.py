def FindIntersection(str_arr):
    """Find the intersection of two comma-separated strings

    :param str_arr: An array of two comma-separated strings
    :return: comma-separated string containing the numbers that occur in
    elements of strArr in sorted order
    """
    if not str_arr or len(str_arr) != 2:
        return False

    list_str_x = str_arr[0].replace(' ', '').split(',')
    list_str_y = str_arr[1].replace(' ', '').split(',')

    list_x = [int(item) for item in list_str_x]
    list_y = [int(item) for item in list_str_y]

    intersection = list(set(list_x).intersection(list_y))

    if not intersection:
        return 'false'

    intersection.sort()

    return ','.join([str(item) for item in intersection])
