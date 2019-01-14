
from insertion_sort import insertion_sort

def main():

    list = [12,11,13,5,6]
    insertion_sort(list)

    for i in range(len(list)):
        print ("%d" %list[i])

if __name__ == "__main__":
    main()
