def check_palindrome(str):
    for i in range(len(str)//2):
        if str[i] != str[len(str)-1-i]:
            return False
    return True

user_input = input("Enter a string: ")
if check_palindrome(user_input):
    print(f'"{user_input}" is a palindrome.')
else:
    print(f'"{user_input}" is not a palindrome.')