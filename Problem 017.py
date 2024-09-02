def number_to_words(n):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
            "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
            "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if n < 20:
        return ones[n]
    elif n < 100:
        return tens[n // 10] + (ones[n % 10] if n % 10 != 0 else "")
    elif n < 1000:
        return ones[n // 100] + "hundred" + (("and" + number_to_words(n % 100)) if n % 100 != 0 else "")
    elif n == 1000:
        return "onethousand"
    else:
        return ""

def count_letters_in_numbers(limit):
    total_letters = 0
    for i in range(1, limit + 1):
        words = number_to_words(i)
        total_letters += len(words)
    return total_letters

limit = 1000

result = count_letters_in_numbers(limit)

print(result)
