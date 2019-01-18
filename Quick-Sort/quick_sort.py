# O(n)^2 Worst Case
def partition(arr, left, right, pivot):
    ''' Helper function to sort a chunk of unsorted array with a pivot'''

    # move from left to right simoultaneously
    while left <= right:
         # move left until you find an element that is bigger than the pivot
        while arr[left] < pivot:
             left += 1

        # move right until you find an element that is smaller than the pivot
        while arr[right] > pivot:
            right -= 1

        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return left


def quick_sort(arr, left, right):

    if left >= right:
        return
    else:
        pivot = arr[(left+right)/2]
        partition_point = partition(arr, left, right, pivot)
        quick_sort(arr,left, partition_point-1)
        quick_sort(arr,partition_point, right)


'''
        ALGORITHM
        *********

        Part I. Inside Quik Sort Funtion
        ********************************

        - Check if left is less or equla to right
            - if so...
                - return
            - otherwise
                - set the a pivot to the middle element of the list
                - call the partition method with the array, the left, right, and pivot to get the partition point
                - call the quicksort(recursive) on left elements
                - call the quicksort(recursive) on right elements


        Part II. Inside Partition Function
        **********************************

        - while left(index) is less than or equal to the right(index)
            - move left until you find an element that is bigger than the pivot
                - increment left by one each time the current left element is less than the pivot
            - move right until you find an element that is smaller than the pivot
                - increment left by one each time the current left element is less than the pivot

            - check if left index is less or equall to right index
                - if yes...
                    - swap the values of arr at left with the one at right
                    - increment left by one
                    - decrement right by one

        - return the dividing point between left and right side
'''
