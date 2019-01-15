# Insterion sort
# Best Case Scenario : O(n) if the list is already sorted 
# Worst Case scenario : O(n)^2

def insertion_sort(list):

    for i in range(1, len(list)):
        current_element = list[i]
        previous_index = i-1
        # Shifts elements of list[0..i-1], that are greater than the current element to 1 up.
        while previous_index >= 0 and current_element < list[previous_index]:
            list[previous_index+1] = list[previous_index]
            previous_index -= 1

        list[previous_index+1] = current_element
