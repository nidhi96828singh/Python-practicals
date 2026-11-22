

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Enter a number: "))
print(n, "is prime" if is_prime(n) else "is not prime")

lo = int(input("Range start: "))
hi = int(input("Range end: "))
print("Primes:", [x for x in range(lo, hi + 1) if is_prime(x)])
