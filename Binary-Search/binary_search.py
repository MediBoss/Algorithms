# Binary Search : Search a sorted array by repeatedly dividing the search interval in half

def binary_search(list,item):
    """
    @param list: The list of elements
    @param item: The element to be searched in the list
    Time complexity :
    Best Case Scenario : The list is sorted
    Worst Case Scenario:

    """

    low = 0
    high = len(list)
    while low <= high:
        middle = int((low + high)/2))
        if list[middle] == item:
            return middle
