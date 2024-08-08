# decimal to binary

def bin(a):
    assert int(a) == a, "Integers Only"
    if a == 0:
        return 0
    else:
        return 10 * bin(int(a/2)) + a%2

print(bin(103))