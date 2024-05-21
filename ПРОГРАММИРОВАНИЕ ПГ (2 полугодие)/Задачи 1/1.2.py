def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def calculate_prime_sum(a, b):
    return sum(i for i in range(a, b + 1) if is_prime(i))

a = int(input("Enter the start of the range: "))
b = int(input("Enter the end of the range: "))
print(f"The sum of all prime numbers between {a} and {b}: {calculate_prime_sum(a, b)}")
