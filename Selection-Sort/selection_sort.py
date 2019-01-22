# Best Case : O(n) ^2 even if list is sorted, we must still check each element with 2 inner loops
# Worst Case : O(n) ^ 2 since we must traverse the entire list with 2 inner loops
def selection_sort(arr):
    ''' Sort the elements in arr from left to right'''

    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j],arr[i]

'''
        ALGORITHM:
        *********

1. Start outter Loop from i=0 to length of list
2. Start inner Loop from i=i+1 to length of list
3. Check of current element in inner loop is less than current element in outter loop
4 If yes, swap both

'''



    # start at index 0
    # find the smallest item in the list from 1 to n-1
        # after finding, compare elemnt at n with each element of array
            # if smaller that current_small element
                # swap
