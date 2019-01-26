
def permutate(string, left, right):

    # Base Case
    if left == right:
        print(str(string))
    else:
        # Recursive case
        for i in range(left, right + 1):
            string[left],string[i] = string[i], string[left]
            permutate(string, left+1, right)
            string[left],string[i] = string[i], string[left]

def main():

    string = "abc"
    print(permutate(list(string),0, len(string)-1))

if __name__ == "__main__":
    main()
