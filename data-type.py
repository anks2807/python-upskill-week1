# Task 1: Data Types

# Converting float to int and print the value
print(int(3.75))

# Converting string to int and print the value
print(int("123"))


# Converting int to boolean and print the value
print(bool(0))

# Converting boolean to string and print the value
print(f"{False}")

# Converting the string to upper case
print("hello".upper())

# addition of numbers and determine type of sum and then type conversion
x= 5
y = 3.14
z = x + y
print(type(z))
print(f"sum after conversion is {int(z)}")


# perform operation on string
s = 'hello'
print(s.upper())
new_s = s.replace('e', 'a')
print(new_s)
print(s.startswith('he'))
print(s.endswith('lo'))