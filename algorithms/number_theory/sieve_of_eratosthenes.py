from math import sqrt


def sieve_of_eratosthenes(n):
    is_prime = [True for x in range((n + 1))]
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, int(sqrt(n)) + 1):
        if is_prime[i]:
            candidates = []
            j = i ** 2
            while j <= n:
                candidates.append(j)
                j = j + i

            for candidate in candidates:
                is_prime[candidate] = False

    primes = []
    for i in range(len(is_prime)):
        if is_prime[i]:
            primes.append(i)

    return primes
