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

        elif list[middle] > item:
            high = middle - 1 # shifting the highest position to the next number lower than middle

        else:
            low = middle + 1 #shifting the lowest position to the next number bigger than the middle number

    return "Item {} Not found in the List".format(item)
