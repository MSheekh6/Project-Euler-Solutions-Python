total = 0
product = 1

for i in range(1,101):
    product *= i
    
product = str(product)

for i in product:
    total += int(i)
    
print(total)
    
