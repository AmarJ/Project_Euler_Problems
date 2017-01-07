#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.
#By Amar Jasarbasic

#checks if int is palindrom
def is_palindrom(n):
    '''(number)->bool'''
    return str(n) == str(n)[::-1]

def largest_palindrom():
    '''(number)->int'''
    #brute force way, still havn't figured out a more efficient solution
    largest_palin = 0
    for i in range(999, 800, -1):
        for j in range(999, 800, -1):
            if is_palindrom(i * j):
                if (i*j)>largest_palin:
                    largest_palin = i* j
            
    return (largest_palin)

print (largest_palindrom())

    
    
    
