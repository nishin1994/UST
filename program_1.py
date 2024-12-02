# Write a program to compute the frequency of the words from the input.
# The output should output after sorting the key alphanumerically.

def compute_freq(str):
	sub_str_dict = {}
	for i in str.split(" "):
		if i not in sub_str_dict.keys():
			sub_str_dict[i] = 1
		else:
			sub_str_dict[i] += 1
	return sorted(sub_str_dict.items())

def main():
    inp_str = input("Enter the user input to get frequency of words : ")
    x = compute_freq(inp_str)
    print(x)

if __name__ == "__main__":
    main()


# Test functions
def test_1():
    x = compute_freq("Hello Hello Hello Hello")
    if not x[0][0] == "Hello":
        return 1
    elif not x[0][1] == 4:
        return 1

def test_2():
    x = compute_freq("Hello World Hello World")
    if not x[0][0] == "Hello":
        return 1
    elif not x[1][0] == "World":
        return 1
    elif not x[0][1] == 2 or not x[1][1] == 2:
        return 1
    else:
        return 0
