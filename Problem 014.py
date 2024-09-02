def collatz_sequence_length(n, cache):
    original_n = n
    length = 0

    while n != 1:
        if n < len(cache) and cache[n] != 0:
            length += cache[n]
            break

        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1

        length += 1

    cache[original_n] = length

    return length

def find_longest_collatz(limit):
    cache = [0] * (limit + 1)
    cache[1] = 1  

    max_length = 0
    number_with_max_length = 1

    for i in range(2, limit):
        current_length = collatz_sequence_length(i, cache)
        
        if current_length > max_length:
            max_length = current_length
            number_with_max_length = i

    return number_with_max_length

limit = 1000000

result = find_longest_collatz(limit)

print(result)
