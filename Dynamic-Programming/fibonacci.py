def memoize(function):

    memo = {}
    def fib_helper(x):
        if x not in memo:
            memo[x] = function(x)
        return memo[x]
    return fib_helper

@memoize
def fib(n):
    '''
        Time Complexity : O(2^n)
    '''
    if n == 1:
        return 1
    elif n == 0:
        return 0
    return fib(n-1) + fib(n-2)

print(fib(100))