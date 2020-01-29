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
    return 1 - (1/(2**k))


def mprobability(k):
    return 1 - (1/(4**k))


def run_fermat(N, k):
    for i in range(1, k):
        a = random.randint(1, N)
        if mod_exp(a, N-1, N) != 1:
            return 'composite'
    return 'prime'


def run_miller_rabin(N,k):
    for i in range(1, k):
        a = random.randint(1, N)
        exp = N - 1
        if mod_exp(a, N - 1, N) != 1:
            return 'composite'
        while exp > 1 and exp % 2 == 0:
            x = mod_exp(a, exp, N)
            if x != 1 and x != N-1:
                return 'composite'
            exp = exp // 2
    return 'prime'