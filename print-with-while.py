# This script prints all even numbers from 1 to 20 using a while loop.
num = 2
while num <= 20:
    if num % 2 == 0:
        print(f"{num}")
    num += 1


# print odd numbers from 1 to 10
num = 1
while num <= 10:
    if num % 2 == 0:
        num += 1
        continue
    print(f"{num}")
    num += 1


# search for a number in a list using while loop
numbers = [10,20,30,40,50,30]
target = 30
index = 0
while index < len(numbers):
    if numbers[index] == target:
        print(f"Found {target} at index {index}")
        break
    index += 1
