# This is a tester file to benchmark the performance of the linear search
from linear_search import linear_search
from algorithm_timer import timing_function

@timing_function
def tester():
    list_one = [10,20,40,50,56,2,4,5,7,8,10,120,67,45,
    24,27,62,65,78,28,77,69,65,58,66,88,100,73,88,16,
    39,58,68,49,59,72,50,76,6782,36,100,22,17,81,70,42,
    88,85,23,25,42,41,83,43,60,75,46,79,12,18,6,43,
    17,42,56,89,50,94,72,68,43,82,53,82,11,94,63,74,67,
    65,77,96,95,61,85,9,26,91,91,44,83,7,90,71,37,73,85,14]

    print "Number 14 is found at position : {}".format(linear_search(list_one,14))
print(tester())

def main():
    tester() # Output : It took 2.98023223877e-05 seconds to execute

if __name__ == "__main__":
    main()
