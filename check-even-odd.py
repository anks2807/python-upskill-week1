#determine the input number is even or odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")


# Find 2 numbers where result is equal to the target number
numbers = [1, 2, 3, 4, 5]
target = 9

for n in numbers:
    diff = target - n
    if diff in numbers and diff != n:
        print(f"Numbers found: {[n, diff]}")
        break

# print fibonacci series up to n terms
n_terms = int(input("Enter number of terms for Fibonacci series: "))
fib = [0, 1]
for i in range(2, n_terms):
    next_term = fib[i-1] + fib[i-2]
    fib.append(next_term)

print(f"Fibonacci seq for {n_terms} is {fib}")