import math

def isPrime(x):
    rv = True
    for i in range(2, int(math.ceil(math.sqrt(x)))+1):
        if x % i == 0:
            rv = False
            break
    return rv

# factor - actual number that is used to cross off multiples throughout
# the list.
# counter - the amount of times the factor needs to multiply to
# get its next multiple; always re-initialized to 1 after reaching each value.
# index - the number of the index that needs to be crossed off,
# and is calculated based on the factor * the counter + the actual index i of
# the list to account for the offset.
def sieve(n):
    l = [True] * n
    primeCounter = 0
    for i, value in enumerate(l):
        if value:
            counter = 1
            factor = i+2
            primeCounter += 1
            index = (factor * counter) + i
            while index < len(l):
                l[index] = False
                counter += 1
                if (factor * counter) + 1 < len(l):
                    index = (factor * counter) + i
                else:
                    break
    return l

# Outputs the prime numbers in list l found by the sieve algorithm
def output(l):
    for g, j in enumerate(l):
        if j is True:
            print(g+2)

def runSieve():
    primes = sieve(1299708)

def main():
    current = 3
    l = [2]
    while len(l) < 100000:
        if isPrime(current):
            l.append(current)
        current += 1

if __name__ == '__main__':
    from timeit import Timer
    n = 5


    print('Finding 100000 prime numbers by Sieve of Eratosthenes where n = {}.'
          .format(n))
    t = Timer('runSieve()', 'from __main__ import runSieve')
    print('Sieve of Eratosthenes took {0:.3f} seconds on average.'
          .format(t.timeit(n) / float(n)))
    
    print('')

    print('Finding 100000 prime numbers by trial division where n = {}'
          .format(n))
    t = Timer('main()', 'from __main__ import main')
    print('Trial division took {0:.3f} seconds on average.'
          .format(t.timeit(n) / float(n)))

    



