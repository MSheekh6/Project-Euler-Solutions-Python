def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def sum_of_prime(n):
    total = 0
    num = 2  
    while num < n:
        if is_prime(num):
            total += num
        num += 1
    return total

limit = 2000000
prime_sum = sum_of_prime(limit)
print(prime_sum)
