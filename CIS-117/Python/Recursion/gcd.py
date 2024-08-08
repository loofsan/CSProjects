# Greatest Common Factor
from re import A


def gcf(n, b):
    assert int(n) == n and int(b) == b, "Must be Positive Integers"
    if n < 0:
        a = a * -1
    if b < 0:
        b = b * -1
    if b == 0:
        return n
    else:
        return gcf(b, n%b)

print(gcf(-48, 1.8))