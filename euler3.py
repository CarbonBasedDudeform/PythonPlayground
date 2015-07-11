#crappy solution to a project euler problem
#main issue is that it continues searching after it has found the answer

num = 600851475143

def isPrime(n):
    for x in range(2, n):
        if ((n % x) == 0):
            return False

    return True


largest = 1
for y in range(2, num//80000000):
    if (isPrime(y) and num % y == 0):
        print ("New largest found", y)
        largest = y

print (largest)
