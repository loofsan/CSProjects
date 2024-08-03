def int_to_reverse_binary(num):
    bString = ""
    while num > 0:
        bString += str(num%2)
        num = num // 2
    return bString

def string_reverse(line1):
    return line1[::-1]
        

if __name__ == '__main__':
    # Type your code here. 
    # Your code must call int_to_reverse_binary() to get 
    # the binary string of an integer in a reverse order.
    # Then call string_reverse() to reverse the string
    # returned from int_to_reverse_binary().
    user_input = int(input())
    output = int_to_reverse_binary(user_input)
    output = string_reverse(output)
    print(output)
    
    

