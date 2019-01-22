from bubble_sort import bubble_sort

def main():

    arr = [9,2,6,4,3,5,1,4,6,3,7]
    bubble_sort(arr)

    for i in range(len(arr)):
        print ("%d" %arr[i])

if __name__ == '__main__':
    main()
