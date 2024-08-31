import math

def count_divisors(n):
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2
    return count

def find_triangle_number_with_divisors(limit):
    n = 1
    while True:
        triangle_number = n * (n + 1) // 2
        if count_divisors(triangle_number) > limit:
            return triangle_number
        n += 1

result = find_triangle_number_with_divisors(500)
print(result)
