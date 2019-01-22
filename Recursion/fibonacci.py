def fibo(number):

    if number < 2:
        return number
    else:
        return fibo(number - 1) + fibo(number - 2)

def main():

    print(fibo(6))

if __name__ == '__main__':
    main()
