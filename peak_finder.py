
# One dimensional problem - Find the peak if it exists Worst Case : O(n)
def find_peak_naive(arr): 

    for index, num in enumerate(arr): 
        if index == 0:
            if arr[index] >= arr[index + 1]:
                return num
        elif index == len(arr) -1 :
            if arr[index] >= arr[index - 1]:
                return num
        if (arr[index] >= arr[index - 1]) and (arr[index] >= arr[index + 1]):
           return num

# One dimensional problem - Find the peak if it exists Worst Case : O(log n)
def find_peak_improved(arr):

    if len(arr) == 1:
        return arr[0]
    else:
        middle = len(arr) // 2
        if (arr[middle] < arr[middle] - 1):
            find_peak_improved(arr[0:middle-1]) 
        elif (arr[middle] < arr[middle + 1]):
            find_peak_improved(arr[middle+1:])
        else:
            return arr[middle]


# 2 dimensional problem - Find the peak if it exists Worst Case : 
def find_peak_2d_greedy (matrix): # O(n*m) where n is row, m is column
    
    peaks = []
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            pass


def find_peek_improved(matrix):

    pass
    # find the middle column j = m/2
    # Find global max on column j at (i,j)
    # compare (i,j-1), (i,j), (i,j+1)
    # pick left columns if (i,j-1) > (i,j)
    # pick the right columns if (i, j+1) > (i,j)
    # else (i,j) is your peak


    
def main():

    arr = [7,3,2,4,8]
    matrix = [
        [3,4,9,1],
        [14,13,12,9],
        [13,9,11,17],
        [16,17,19,20]
    ]
    #print("Peak : ", find_peak_naive(arr))
    print("Peak : ", find_peak_improved(arr))
    #print("Peak : ", find_peak_2d_greedy(matrix))

if __name__ == "__main__":
    main()