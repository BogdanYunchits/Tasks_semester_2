import re

def check_palindrome(text):
    text = re.sub(r'[^A-Za-z0-9]', '', text).lower()
    return text == text[::-1]

user_input = input("Enter a string: ")
if check_palindrome(user_input):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
