from quick_sort import quick_sort
from quick_sort import partition


def main():

    arr = [9,2,6,4,3,5,1]
    quick_sort(arr, 0, len(arr)-1)

    for i in range(len(arr)):
        print ("%d" %arr[i])


if __name__ == '__main__':
    main()
