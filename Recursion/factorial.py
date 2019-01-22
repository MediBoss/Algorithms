
'''
    Factorial is the product of an integer and all the integers below it; e.g.
    factorial four (4!) is equal to 24.
    Worst Case : O(n) Linear
'''

def factorial(number):

    # Base case - tells the recursion when to terminate
    if number == 0:
        return 1
    else:
    # Recursive case - calls the function within
        return number * factorial(number - 1)

def main():

    print(factorial(5))

if __name__ == "__main__":
    main()
