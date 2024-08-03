nums = input()
num_list = [float(elem) for elem in nums.split()]
max_num = max(num_list)
average = sum(num_list)/len(num_list)

print(f'{max_num:.2f} {average:.2f}')