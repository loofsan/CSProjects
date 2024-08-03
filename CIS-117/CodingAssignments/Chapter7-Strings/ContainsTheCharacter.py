user_char = input()
user_str = input()

user_str = user_str.strip()
user_strList = user_str.split()

for i in user_strList:
    if user_char in i:
        print(i, end=",")