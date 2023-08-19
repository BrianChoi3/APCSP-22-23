num = int(input("What number would you like to find the prime factors of? "))
factors = []
for i in range(2, num):
    while num % i == 0:
        factors.append(i)
        num = num / i
print(factors)
