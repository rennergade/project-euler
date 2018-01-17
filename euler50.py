from prime import primes1

def add_primes(primes, count):
    in_counter = 0
    sum = 0
    L = []
    while sum < 1000000:
        sum = sum + primes[count]
        if sum in primes:
            L.append(sum)
        in_counter += 1
        count += 1
    if L[-1] < 1000000:
        return L[-1], in_counter
    elif L[-1] > 1000000:
        print "****"
        return L[-2], in_counter

def main():
    primes = primes1(1000000)
    main_counter = 0
    for count in range(0, 20):
        x = add_primes(primes, count)
        print x[0], x[1]
        if x[0] > main_counter:
            main_counter = x[0]
    print "Answer = ", main_counter

if __name__ == '__main__':
    main()
