# Sum Of Digits

def pos(n):
    assert n>=0 and int(n) == n , "The number has to be a positive integer only."
    if n == 0:
        return 0
    else:
        return int(n%10) + pos(n/10)

print(pos(18))

