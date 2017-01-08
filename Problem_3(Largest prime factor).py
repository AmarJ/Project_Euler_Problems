#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
#By Amar Jasarbasic

def largest_prime_factor(n):
    '''(int)->int'''

    largest_factor = 0
    counter = 2

    #this is pretty much just prime factorization  

    while (counter**2 <= n):
        if n%counter == 0:
            n = (n / counter)
            largest_factor = counter
        else:
            counter += 1

    if (n > largest_factor):
        largest_factor = n

    return (int(largest_factor))

print (largest_prime_factor(600851475143))
