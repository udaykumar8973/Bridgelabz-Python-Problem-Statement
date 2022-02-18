num = int(input("Enter the number for calculating the prime factors :\n"))

def prime_fact(num):
    prime_factors = []
    divisor = 2
    while divisor <= num:
        if num % divisor == 0:
            prime_factors.append(divisor)
            num /= divisor
        else:
            divisor += 1
    return prime_factors

print(prime_fact(num))