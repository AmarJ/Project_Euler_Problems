#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def is_div(n):
    for i in range(11, 21):
        if n%i != 0:
            return False
    return True

#since we know that the smallest number that can divided by numbers 1-10 is 2520, we start there.

smallest_num = 1

for i in range(2520, 10000000000, 2520):
    smallest_num = smallest_num*i
    print (smallest_num)
    if is_div(smallest_num):
        print ("smallest sum is:", smallest_num)
        break
