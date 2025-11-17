# Task 2: input and print

#Greet the user
user_name = input("Enter your name")
print(f"Hello, {user_name}")

#Arthmetic operations
a = int(input("enter first number"))
b = int(input("enter second number"))

print(f"Sum: {a+b}")
print(f"Multiplication: {a*b}")
print(f"Division: {a/b}")

#copy the entered name to list
names = input("Input comma separated names:")
name_list = [name.strip() for name in names.split(",")]
print(name_list)

# Eligiblity to vote
age = int(input("enter your age"))
if age >= 18:
    print("You can cast your vote")
else:
    print("You are not eligible")


#round the float number
f = 3.14159
print(f"{round(f, 2)}")