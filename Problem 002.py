total = 0
a = 1
b = 2
while a <= 4000000 :
    if a % 2 == 0:
        total += a
    a,b = b, a + b
print(total)
    
