
# This is a tester file to benchmark the performance of the binary search
from binary_search import binary_search
from algorithm_timer import timing_function


@timing_function
def tester():
    item = 64
    list_one = [10,20,40,50,56,60,64,75,87,88,90,92,97,105]

    print "Number {} is found at position : {}".format(item,binary_search(list_one,item))
print(tester())

def main():
    tester()
    # Output : when item is 10 : it took 5 seconds
    # Ouput : when item is 64 : 3 seconds

if __name__ == "__main__":
    main()
