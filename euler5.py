def divisableByAll(n, upper):
    for x in range(1, upper):
        if (n % x != 0):
            return False

    return True

x = 2520
while (divisableByAll(x, 20) == False):
    x = x + 10

print(x)
