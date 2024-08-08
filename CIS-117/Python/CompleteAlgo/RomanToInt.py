#Solution 1

def romanToInt(s):
    dict = {"I": 1, "V": 5, "X": 10, "L": 50,
    "C": 100, "D": 500, "M": 1000}
    num = 0
    list = []
    for i in s:
        list.append(i)
    for n in range(len(list)):
        if n == 0:
            num += dict[list[n]]
        elif dict[list[n]] > dict[list[n-1]]:
            num += dict[list[n]] - 2*dict[list[n-1]]
        else:
            num += dict[list[n]]
            

    print(num)


romanToInt("MCMXCIV")