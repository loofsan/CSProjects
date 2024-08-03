user_input = int(input())
if user_input < 11 or user_input > 99:
    print("Input must be 11-99")
elif user_input == 11:
    print(user_input)
else:
    for i in range(user_input, 0, -1):
        print(i)
        if (i//10) == (i%10):
            break
