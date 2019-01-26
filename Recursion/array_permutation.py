'''
Given an array of integers, return the set of all permutations.

'''

def permutate(arr):

    # Base Case
    if len(arr) <= 1:
        return [arr]

    # Recursive Case
    else:

        last_element = arr[-1]
        result = permutate(arr[:-1])
        permutations = []
        for p in result:
            for i in range(len(arr)):
                left = p[:i]
                right = p[i:]
                permutations.append(left + [last_element] + right)

    return permutations

def main():

    list_one = [1,2]
    list_two = [1,2,3]

    permutate(list_one)


if __name__ == "__main__":
    main()
