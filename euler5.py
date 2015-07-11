def divisableByAll(n, upper):
    for x in range(1, upper):
        if (n % x != 0):
            return False

    return True

x = 2520 #lowes divisible by [1..10]
while (divisableByAll(x, 20) == False):
    x = x + 20
    #go up in increments of the largest number it must be divisible by
    #to increase the speed, also because i figure it must,
    #19/20 will obviously never be divisible by 20, so it must at least be 20 initially
    #likewise, if 2520 isn't divible by all [1..20] then 2520 + 19 won't be, as it'll still
    #not be divisible by 20, you'll have 1/20 remainder

print(x)
