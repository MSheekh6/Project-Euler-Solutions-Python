def is_palindrome(number):
    return str(number) == str(number)[::-1]

def largest_palindrome_product():
    max_palindrome = 0
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            product = i * j
            if is_palindrome(product) and product > max_palindrome:
                max_palindrome = product
    return max_palindrome

largest_palindrome = largest_palindrome_product()
print(largest_palindrome)
