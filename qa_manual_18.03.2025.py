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

# task2
# while True:
#     user_number_1 = float(input("Enter 1 number: "))
#     user_number_2 = float(input("Enter 2 number: "))
#     user_activity = input("Enter math operator (+, -, *, /): ")
#
#     if user_activity == "+":
#         result = user_number_1 + user_number_2
#     elif user_activity == "-":
#         result = user_number_1 - user_number_2
#     elif user_activity == "*":
#         result = user_number_1 * user_number_2
#     elif user_activity == "/":
#         if user_number_2 == 0:
#             result = 'non-existent'
#             print("You can't divide by 0")
#         else:
#             result = user_number_1 / user_number_2
#     else:
#         result = 'non-existent'
#         print("Error: change math operator")
#
#     print(f"Result is {result}")
#
#     next_use = input("Would you like to make another calculation? (yes/no): ").strip().lower()
#     if next_use not in ["yes", "y"]:
#         print("It was nice to assist you!")
#         break
