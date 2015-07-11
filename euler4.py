def isPalindrome(x):
    l = len(str(x))
    s = str(x)
    for n in range(l):
        if (s[n] != s[l-n-1]):
            return False

    return True

upper = 1000
lower = 100
biggest = 0
for x in range(lower, upper):
    for y in range(lower, upper):
        if (isPalindrome(x*y)):
            if x*y > biggest:
                biggest = x*y

print biggest
