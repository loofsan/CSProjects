def power(base, exp):
    assert exp >= 0 and int(exp) == exp, "Positive Integers Only for exponents"
    if exp == 0:
        return 1
    if exp == 1:
        return base
    else:
        return base * power(base, exp-1)

print(power(-3.5, 3))