
# Worst case : O(n)^2 if we must traverse the entire nested loop
# Best case : O(n) if the list is already sorted

def bubble_sort(arr):

    num_of_iterations = len(arr) - 1
    for i in range(num_of_iterations):
        for j in range(num_of_iterations):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

'''
        ALGORITHM
        *********
    Main Idea: Compare adjacent elements in the list, each time putting
    in the righ order of magnitude, only two elements.

    1. Get the number of iterations by substracting the length of the array by 1selfself.
        - Example : if arr[3,2,1], it would take us two swaps to sort the list

    2. The outter and inner loop makes sure we only traverse within the number of ietrations
    3. If the element adjacent is greater than the current, we swap them

    ** NOTE: Bubble Sort should not be used on larger data sets

'''
