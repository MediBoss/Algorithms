
def partition(unsoted_arr, first_index, last_index):
    ''' Helper function to sort the chopped array with a pivot'''

    pivot_element = unsoted_arr[first_index]
    pivot_index = first_index
    index_of_last_element = last_index
    greater_than_pivot_index = first_index + 1
    less_than_pivot_index = index_of_last_element

    while True:

        while unsoted_arr[greater_than_pivot_index] < pivot and greater_than_pivot_index < last_index:
            greater_than_pivot_index += 1

        while unsoted_arr[less_than_pivot_index] > pivot and less_than_pivot_index >= first_index:
            less_than_pivot_index -= 1
        



def quick_sort(arr):
    pass






'''
        ALGORITHM
        *********




'''
