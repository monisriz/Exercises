# sum of numbers below 1000 which are multiples of 3 or 5:

sum = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
print("Sum of all multiples of 3 or 5 below 1000: ",sum)
