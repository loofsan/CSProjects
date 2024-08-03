num1 = int(input())
num2 = int(input())
num3 = int(input())

num_list = [num1, num2, num3]

min_num = min(num_list)

num_list= [num1-min_num, num2-min_num, num3-min_num]

print(num_list[0], num_list[1], num_list[2])