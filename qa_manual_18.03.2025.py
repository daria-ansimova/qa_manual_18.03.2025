import keyword
import string

user_variable_name = input("Enter variable name: ")

if user_variable_name:
    if user_variable_name[0].isdigit():
        print("False")
    elif any(char in string.ascii_uppercase for char in user_variable_name):
        print("False")
    elif keyword.iskeyword(user_variable_name):
        print("False")
    elif any(char in string.punctuation.replace("_", " ") for char in user_variable_name):
        print("False")
    elif '__' in user_variable_name[1:]:
        print("False")
    elif user_variable_name == '__':
        print("False")
    else:
        print("True")
else:
    print("False")