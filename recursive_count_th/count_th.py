'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    # base case
    if len(word) < 2:
        return 0
        # i need to search for "th"
    if word[0:2] == "th":
        return 1 + count_th(word[1:])

    else:
        return 0 + count_th(word[1:])
 # the recursive function will loop through the word and return a count of the occurences of "th"
