
def merge_sort(arr):

    if len(arr) > 1:
        middle_point = len(arr) // 2
        left_half = arr[:middle_point]
        right_half = arr[middle_point:]

        merge_sort(left_side) # sort the left half of the array
        merge_sort(right_side) # sort the right half of the array

        left_index = right_index = current_index = 0
        while left_index < len(left_half) and right_half < len(right_half):

            if left_half[left_index] < right_half[right_half]:
                arr[current_index] = left_half[left_index]
                left_index += 1
            else:
                arr[current_index] = right_half[right_index]
                right_index += 1

        while left_index < len(left_half):
            arr[current_index] = left_half[left_index]
            left_index += 1
            current_index += 1

        while right_index < len(right_half):
            arr[current_index] = right_half[right_index]
            current_index += 1
            right_index += 1

            ''' ALGORITHM
                    Split array in two halves
                    merge sort left side
                    merge sort right side
                    Merge left and right side in sorted order

            '''
