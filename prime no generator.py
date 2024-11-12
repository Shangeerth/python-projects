def generate_primes(n):
    primes = []
    num = 2  # Start with the first prime number

    while len(primes) < n:
        is_prime = True
        # Check if num is divisible by any number from 2 to num-1
        for i in range(2, num):
            if num % i == 0:
                is_prime =False
                break

        # If num is prime, add it to the list
        if is_prime:
            primes.append(num)
        
        num += 1  # Move to the next number

    return primes

# Input for the number of prime numbers you want to display
n = int(input("Enter the number of prime numbers to display: "))
print(generate_primes(n))
