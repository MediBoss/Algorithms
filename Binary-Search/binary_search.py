# Binary Search : Search a sorted array by repeatedly dividing the search interval in half

# Iterative binary serach
def binary_search(list,item):
    """
    @param list: The list of elements
    @param item: The element to be searched in the list
    Best Case Scenario : O(1) item is in the middle of the list
    Worst Case Scenario: O(n) does not appear in the list at all

    """

    low = 0
    high = len(list)
    while low <= high:
        middle = int((low + high)/2)
        if list[middle] == item:
            return middle
        elif list[middle] > item:
            high = middle - 1 # shifting the highest position to the next number lower than middle
        else:
            low = middle + 1 #shifting the lowest position to the next number bigger than the middle number

    return "Item {} Not found in the List".format(item)


# Recursive Binary Search
def recursive_binary_search(list, item, low, high):

    if high >= low:
        middle = low + (high - 1)/2
        if list[middle] == item:
            return middle
        elif list[middle] > item:
            high = middle - 1
            return recursive_binary_search(list[low:high], item, low, high)
        else:
            low = middle + 1
            return recursive_binary_search(list[low:high], item, low, high)
    else:
        return -1
