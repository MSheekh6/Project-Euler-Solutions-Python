sum_of_squares = 0
total = 0
square_of_sums = 0
for  i in range(0,101):
    squared = i ** 2
    total += i
    sum_of_squares += squared
square_of_sums = total ** 2
diff = sum_of_squares - square_of_sums
print(abs(diff))
    
    
