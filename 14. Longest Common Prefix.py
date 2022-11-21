def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    # get the smallest string
    smallest_string = strs[0]
    for i in strs:
        if (len(i) < len(smallest_string)):
            smallest_string = i

    length = len(smallest_string)
    # start at the end of the string
    # if there is a mismatch, remove it
    for i in range(len(smallest_string) - 1, -1, -1):
        remove = False
        for other in strs:
            print("current:", smallest_string[:length])
            if other[i] != smallest_string[i]:
                length = i

    return smallest_string[:length]


print(longestCommonPrefix(["cir", "car"]))
