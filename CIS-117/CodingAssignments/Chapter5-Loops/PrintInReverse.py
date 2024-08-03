while True:
    user_input = input()
    if user_input in ["Done", "done", "d"]:
        break
    for i in reversed(user_input):
        print(i, end="")
    print('')