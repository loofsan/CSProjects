is_leap_year = False
   
input_year = int(input())
if input_year % 4 == 0:
    if (input_year%10 == 0) and (input_year%100 == 0):
        if (input_year % 400 == 0):
            is_leap_year = True
            print(f'{input_year} - leap year')
        else:
            print(f'{input_year} - not a leap year')
    else:
        print(f'{input_year} - leap year')
else:
    print(f'{input_year} - not a leap year')
