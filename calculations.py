from math import log


def primes_list(n):
    """
    This function returns all the primes that are up to the given number.

    :param n:
    :return a list of all the primes up to that number:
    """
    pr_list = list(range(2, n+1))
    indices = len(pr_list)*[True]
    for pointer in range(len(pr_list)-1):
        if indices[pointer]:
            num = pr_list[pointer]
        for k in range(pointer+1, len(pr_list)):
            if pr_list[k] % num == 0:
                indices[k] = False
    return [pr_list[i] for i in range(len(pr_list)) if indices[i]]


def prime_exponents(n, list_of_primes=None):
    """
    This function returns the exponents of the prime decomposition of a given number given a list of primes or all
    the primes up to the given number if a list of primes is not given.
    :param n:
    :param list_of_primes:
    :return a list of the exponents of the prime decomposition of n:
    """
    if list_of_primes is None:
        primes_lst = primes_list(n)
    else:
        primes_lst = list_of_primes

    exponents = [0]*len(primes_lst)
    for i in range(len(primes_lst)):
        exponent = 1
        while n % (primes_lst[i]**exponent) == 0:
            exponent += 1
        exponents[i] = exponent-1
    return exponents


def choose(n, k):
    if n < k:
        return None
    if n == k:
        return 1
    list_of_primes = primes_list(n)
    print(list_of_primes)
    exponents = len(list_of_primes)*[0]
    print(exponents)
    m = max(k, n-k)
    for num in range(m+1, n+1):
        exponents = [x+y for x, y in zip(exponents, prime_exponents(num, list_of_primes))]
        print(exponents)
    for num in range(2, n-m+1):
        exponents = [x-y for x, y in zip(exponents, prime_exponents(num, list_of_primes))]
        print(exponents)
    print(exponents)

    result = 1
    print("result: {}".format(result))
    for i in range(len(list_of_primes)):
        print("prime: {} - exp: {}".format(list_of_primes[i], exponents[i]))
        if list_of_primes[i] * exponents[i] > 0:
            result *= list_of_primes[i] * exponents[i]
        print("result: {}".format(result))
    print(list_of_primes)
    print(exponents)
    return result
