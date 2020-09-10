prime_numbers = [x for x in range(2, 1000) if all([x % i != 0 for i in range(2, x)])]
# print(prime_numbers)
