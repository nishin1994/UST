# Your function should accept a sequence of comma separated passwords
# and will check them according to the above criteria. Passwords that
# match the criteria are to be printed, each separated by a comma
import string

def check_pass(str):
    result = {}
    special_symbols = ["$","#","@"]
    for i in str.split(","):
        check=[0,0,0,0,0]
        if 6<=len(i)<=12:
            check[0] |= 1
        for char in i:
            if char in special_symbols:
                check[4] |= 1
            if char in string.ascii_lowercase:
                check[1]|= 1
            if char in string.ascii_uppercase:
                check[2] |= 1
            if char.isdigit():
                check[3] |= 1
        result[i] = (check[0] and check[1] and check[2] and check[3] and check[4])
    return result

def main():
    inp_str = "Asqwr1234@,aF145#,2w3E*,2We3345"
    result = check_pass(inp_str)
    for i,x in result.items():
        if x:
            print("Password {} is correct".format(i))
        else:
            print("Password {} is not correct".format(i))


if __name__ == "__main__":
    main()

def test_1():
    inp_str = "2w3E*"
    result = check_pass(inp_str)
    if result[0] != 0 or result[1] !=1 or result[2] !=1 or result[3] !=1  or result[4] != 0:
        return 1
    else:
        return 0