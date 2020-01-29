import random


def prime_test(N, k):
    # This is the main function connected to the Test button. You don't need to touch it.
    return run_fermat(N,k), run_miller_rabin(N,k)


def mod_exp(x, y, N):
    if y == 0: return 1                    #
    z = mod_exp(x, y//2, N)                # Will be called log(y) times, since y shrinks by half each iteration.
    if y % 2 == 0:                         # Mod is O(n^2)
        return pow(z, 2) % N               # Multiplication is O(n^2) add the mod and we get O(n^2 + b^2) where n and b are the bits in z and N respectively.
    else:                                  #
        return x * pow(z, 2) % N           # See above. In total this algorithm runs in O(log(n)2n^2) which is n^2.


def fprobability(k):
    return 1 - (1/(2**k))                 # Should run in O(n^2) since division and multiplication are n^2 operations.


def mprobability(k):
    return 1 - (1/(4**k))                 # See above.


def run_fermat(N, k):
    for i in range(1, k):                 # At most k iterations.
        a = random.randint(1, N)          #
        if mod_exp(a, N-1, N) != 1:       # This runs in n^2 time as seen above.
            return 'composite'            #
    return 'prime'                        # Total time is at most O(k * n^2)


def run_miller_rabin(N,k):
    for i in range(1, k):                 # Once again, at most k iterations.
        a = random.randint(1, N)          #
        exp = N - 1                       #
        if mod_exp(a, N - 1, N) != 1:     #
            return 'composite'            # Same complexity as above at this point.
        while exp > 1 and exp % 2 == 0:   # This loop will run at most exp / 2 times - which is really N / 2
            x = mod_exp(a, exp, N)        #
            if x != 1 and x != N-1:       #
                return 'composite'        #
            exp = exp // 2                # Once again a O(n^2) operation.
    return 'prime'                        # Given that the inner loop runs N / 2 times and the outer loop runs k times
                                          #     the complexity looks something like k * N/2.