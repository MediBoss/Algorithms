
# This is a tester file to benchmark the performance of the binary search
from binary_search import binary_search
from binary_search import recursive_binary_search
from algorithm_timer import timing_function


def tester():
    item = 64
    list_one = [10,20,40,50,56,60,64,75,87,88,90,92,97,105]

    print "Number {} is found at position : {}".format(item,binary_search(list_one,item))
    #print "Number {} is found at position : {}".format(item,recursive_binary_search(list_one,item, 0, len(list_one)))

def main():
    tester()

if __name__ == "__main__":
    main()
