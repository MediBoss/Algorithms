# Programmer : Medi Assumani
# Linear sort is commonly used for small range of data in a list since it parses the data one by one.


# Function to lineary look for item in list and returns its location or -1 if it's not found
def linear_search(list, item):
    return (index for index in list if item == list[index])
