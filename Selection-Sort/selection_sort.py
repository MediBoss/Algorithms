
# O(n)
def find_smallest(arr):
    ''' Helper function to find the smallest element in a sequence '''
    min = arr[0]
    for elem in arr:
        if elem < min:
            min = elem

    return min


def selection_sort(arr):

    smallest = find_smallest(arr)
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]






    # start at index 0
    # find the smallest item in the list from 1 to n-1
        # after finding, compare elemnt at n with each element of array
            # if smaller that current_small element
                # swap
