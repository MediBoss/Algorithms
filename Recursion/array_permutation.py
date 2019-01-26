'''
Given an array of integers, return the set of all permutations.

'''

def permutate(arr):

    # Identify base case
    if len(arr) == 0 or len(arr) == 1:
        return arr

    # Identify recursive case
