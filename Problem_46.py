#It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
#9 = 7 + 2×1^2
#15 = 7 + 2×2^2
#21 = 3 + 2×3^2
#25 = 7 + 2×3^2
#27 = 19 + 2×2^2
#33 = 31 + 2×1^2
#It turns out that the conjecture was false.
#What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
#By Amar Jasarbasic

#odd = prime + 2*(x^2)

def prime_gen(n):
    primes = []
    for i in range(2,n+1):
        for j in range(2,i):
            if i%j == 0:
                break    
        else:            
            primes.append(i)
    return primes

def square_gen(n):
    square = []
    for i in range(1,n+1):
        square.append(i**2)
    return square

primes = prime_gen(10000)
squares = square_gen(40)
gold_comp = []

for i in primes:
    for j in squares:
        gold_comp.append(i+(2*j))

for i in range(9, 10000+1, 2):
    if not(i in gold_comp):
        if not(i in primes):
            print (i)
            break


