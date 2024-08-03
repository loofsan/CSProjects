str_input = input()
cleaned_str = str_input.replace(" ", "").lower() 

# Initialize two pointers
left = 0
right = len(cleaned_str) - 1

# Compare characters while moving pointers inward
while left < right:
    if cleaned_str[left] != cleaned_str[right]:
        print(f"not a palindrome: {str_input}")
        break
    left += 1
    right -= 1
    
else:
    print(f"palindrome: {str_input}")