# -*- coding: utf-8 -*-
"""
Code challange #1 - Prime Factorization: 

Write Python function to find all prime factors of an integer number.

Input: integer value 
Output: list of primes
"""

def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True
    
    
def prime_generator(s, e):
    if s > 1 and s <e:
        return [x for x in range(s,e) if is_prime(x)]


def get_prime_factors_1(numb):
    prime_factors = []
    primes = prime_generator(2, numb+1)
    # print(primes)
    i = 0
    while primes[i] <= numb:
        if numb % primes[i] == 0:
            prime_factors.append(primes[i])
            numb = numb // primes[i]
        else:
            i += 1
                   
    return prime_factors


def get_prime_factors(N): ##faster solution
    factors = list()
    divisor = 2
    while(divisor <= N):
        if (N % divisor) == 0:
            factors.append(divisor)
            N = N//divisor
        else:
            divisor += 1
    return factors


# # print(prime_generator(2, 306))
# print(get_prime_factors_1(630))
# print(get_prime_factors_1(13))

# print(get_prime_factors_1(6000030)) #[2, 3, 3, 5, 163, 409]   [Finished in 24.9s]
print(get_prime_factors(6000030)) # [2, 3, 3, 5, 163, 409]   [Finished in 85ms]
# print(get_prime_factors(113))