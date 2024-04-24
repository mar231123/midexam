print("Question no 01 ")
def rev_string(str):
    if len(str) == 0:
        return str
    else:
        return rev_string(str[1:]) + str[0]

string=input("Enter the string to reverse:")
result = rev_string(string)
print(result)

