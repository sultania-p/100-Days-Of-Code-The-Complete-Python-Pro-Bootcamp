n = int(input("Enter the number to check the prime: "))

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False

    if is_prime:
        print(f"The number {number} is a prime number.")
    else:
        print(f"The number {number} is not a prime number.")

prime_checker(number=n)