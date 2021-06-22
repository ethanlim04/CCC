'''
def sieve (start, end):
    arr = {i for i in range(start, end+1)}
    primes = set()
    factors = [i for i in range(2, int((end)**(1/2))+1)]

    for factor in factors:
        endPoint = int(end/factor)
        for i in range(2, endPoint+1):
            try:
                primes.add(i*factor)
            except:
                continue
    out = [*arr-primes-{1}-{0}]
    out.sort()
    return out
'''
def sieve(end):
    largest = end
    sieve = [True] * largest
    for index in range(2, int((largest)**(1/2)) + 1):
        if sieve[index]:
            increment = 0
            while (index ** 2) + index * increment < largest:
                sieve[(index ** 2) + index * increment] = False
                increment += 1
    return [i for i in range(len(sieve)) if sieve[i] and i not in [0, 1]]


def exec(num, primes):
    n = num*2
    start = n - 10**(4)
    if(start < 0):
        start = 0
    end = n
    #print(primes)
    i = 0
    j = len(primes) -1
    while(i != len(primes)-1 and j != 0):
        s = primes[i] + primes[j]
        if(s == n):
            return [primes[i], primes[j]]
        else:
            if(s >= n):
                j -= 1
            elif(s <= n):
                i += 1

output = []
numbers = []
for i in range(int(input(""))):
    num = int(input(""))
    numbers.append(num)
m = max(numbers)
primes = sieve(m*2)
#print(primes)
for n in numbers:
    output.append(exec(n, primes))

for t in output:
    print(*t)
