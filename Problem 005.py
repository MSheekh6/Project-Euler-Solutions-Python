import math

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def lcm_multiple(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result = lcm(result, number)
    return result

numbers = range(1, 21)
smallest_multiple = lcm_multiple(numbers)
print(smallest_multiple)
