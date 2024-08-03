user_string = input()

split_list = [ord(c) for c in user_string]
is_valid = False
for i in split_list:
    if  i >= 48 and i <= 57:
        is_valid = True
    else:
        is_valid = False
        print("No")
        break
if (is_valid):
    print("Yes")