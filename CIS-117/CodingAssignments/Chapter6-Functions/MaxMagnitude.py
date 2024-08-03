def max_magnitude(user_val1, user_val2, user_val3):
    val1 = abs(user_val1)
    val2 = abs(user_val2)
    val3 = abs(user_val3)
    current_max = max(val1, val2)
    max_value = max(current_max, val3)
    if max_value == abs(user_val1):
        return user_val1
    elif max_value == abs(user_val2):
        return user_val2
    elif max_value == abs(user_val3):
        return user_val3

'''
def max_magnitude(user_val1, user_val2, user_val3):
    # Find the absolute values of the input values
    abs_val1 = abs(user_val1)
    abs_val2 = abs(user_val2)
    abs_val3 = abs(user_val3)
    
    # Determine the value with the largest magnitude
    if abs_val1 >= abs_val2 and abs_val1 >= abs_val3:
        return user_val1
    elif abs_val2 >= abs_val1 and abs_val2 >= abs_val3:
        return user_val2
    else:
        return user_val3
'''



if __name__ == '__main__':
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    print(max_magnitude(num1, num2, num3))