# My first approach

def is_palindrome(product):
    arr = [n for n in map(int, str(product))]
    arr_len = len(arr)
    half_arr_len = int(len(arr)/2)+1

    for i in range(0, half_arr_len):
        if arr[i] != arr[arr_len - 1 - i]:
            return False
    return True


def find_biggest_palindrome():
    palindromes = []
    for i in range (1000, 100, -1):
        for j in range(1000, 100, -1):
            product = i * j
            if (is_palindrome(product)):
                palindromes.append(product)
    print(f"Biggest palindrome #1st approach: {max(palindromes)}")
    return max(palindromes)


find_biggest_palindrome()

# My second approach:
# Once I learned that string can be easily reversed in Python
# in just one line of code this became much shorter:


def find_biggest_palindrome_2():
    palindromes = []
    for i in range (1000, 100, -1):
        for j in range(1000, 100, -1):
            if str(i * j) == str(i * j)[ : : -1]:
                palindromes.append(i * j)
    print(f"Biggest palindrome #2nd approach: {max(palindromes)}")
    return max(palindromes)


find_biggest_palindrome_2()


# My third approach:

palindromes = [(i * j) for i in range (1000, 100, -1) for j in range(1000, 100, -1) if str(i * j) == str(i * j)[ : : -1]]
print(f"Biggest palindrome #3rd approach: {max(palindromes)}")
