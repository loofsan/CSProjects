# TODO: Write recursive digit_count() function here.
def digit_count(n):
    # Base case: If n is less than 10, it has only 1 digit
    if n < 10:
        return 1
    # Recursive case: Count digits by dividing n by 10
    else:
        return 1 + digit_count(n // 10)


if __name__ == '__main__':
    num = int(input())
    digit = digit_count(num)
    print(digit)