
def partition(unsorted_arr, first_index, last_index):
    ''' Helper function to sort a chunk of unsorted array with a pivot'''

    pivot_element = unsorted_arr[first_index]
    pivot_index = first_index
    index_of_last_element = last_index
    greater_than_pivot_index = first_index + 1
    less_than_pivot_index = index_of_last_element

    while True:

        while unsorted_arr[greater_than_pivot_index] < pivot and greater_than_pivot_index < last_index:
            greater_than_pivot_index += 1

        while unsorted_arr[less_than_pivot_index] > pivot and less_than_pivot_index >= first_index:
            less_than_pivot_index -= 1

        if greater_than_pivot_index < less_than_pivot_index:
            unsorted_arr[greater_than_pivot_index], unsorted_arr[less_than_pivot_index] = unsorted_arr[less_than_pivot_index], unsorted_arr[greater_than_pivot_index]
        else:
            break

    unsorted_arr[pivot] = unsorted_arr[less_than_pivot_index]
    unsorted_arr[less_than_pivot_index] = pivot

    return less_than_pivot_index




def quick_sort(arr):
    pass






'''
        ALGORITHM
        *********




'''
