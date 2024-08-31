def find_pythagorean_triplet(sum_total):
    for a in range(1, sum_total // 3):
        for b in range(a + 1, sum_total // 2):
            c = sum_total - a - b
            if a**2 + b**2 == c**2:
                return a, b, c

sum_total = 1000
a, b, c = find_pythagorean_triplet(sum_total)
product = a * b * c

print(product)
