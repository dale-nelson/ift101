#entering 0 doesn't work...

def main():
    print("Please give me a number and I will check if it is even or odd.")
    tmp2_var = loop_until_valid()
    tmp_var = even_or_odd(tmp2_var)
    if tmp_var != 0:
        print("{0} is odd.".format(tmp2_var))
    else:
        print("{0} is even.".format(tmp2_var))
    return

def even_or_odd(num):
    return num % 2

def check_if_valid():
    try:
        return int(float(input()))
    except ValueError:
        print("That is not a number, please try again.")
    return

def loop_until_valid():
    valid_var = check_if_valid()
    while valid_var is None:
        valid_var = check_if_valid()
    else:
        return valid_var

main()