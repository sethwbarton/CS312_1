import random


def prime_test(N, k):
    # This is the main function connected to the Test button. You don't need to touch it.
    return run_fermat(N,k), run_miller_rabin(N,k)


def mod_exp(x, y, N):
    if y == 0: return 1
    z = mod_exp(x, y//2, N)
    if y % 2 == 0:
        return pow(z, 2) % N
    else:
        return x * pow(z, 2) % N

    

def fprobability(k):
    # You will need to implement this function and change the return value.
    return 1 - (1/(2**k))  # The real probability is <= this value. How do I represent that?


def mprobability(k):
    # You will need to implement this function and change the return value.   
    return 0.0


def run_fermat(N, k):
    # You will need to implement this function and change the return value, which should be
    # either 'prime' or 'composite'.
    #
    # To generate random values for a, you will most likley want to use
    # random.randint(low,hi) which gives a random integer between low and
    #  hi, inclusive.
    a = []
    for num in range(1, k):
        a.append(random.randint(1, N))
    isPrime = True
    for num in a:
        if mod_exp(num, N-1, N) != 1:
            isPrime = False
    if isPrime:
        return 'prime'
    else:
        return 'composite'


def run_miller_rabin(N,k):
    # You will need to implement this function and change the return value, which should be
    # either 'prime' or 'composite'.
    #
    # To generate random values for a, you will most likley want to use
    # random.randint(low,hi) which gives a random integer between low and
    #  hi, inclusive.

    # choose a random test, a, in range 1 to N
    # calculate a^n-1 mod N
    # take the square root of  it. Is it 1 or -1? This is a^n-1^1/2
    # now take the square root again. Is it 1 or -1?
    # Keep taking square roots until you get not 1 or -1.
    a = []
    for num in range(1, k):
        a.append(random.randint(1, N))
    for num in a:
        x = mod_exp(a, k, N)
        if x == 1 or x == N-1:
            continue



    return 'composite'