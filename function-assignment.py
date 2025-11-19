def calculate_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width

def calculate_factorial(n):
    """Calculate the factorial of a number."""
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)

def reverse_string(s):
    """Reverse a given string."""
    return s[::-1]

def sum_of_list_element(list1= [], list2= []):
    """Sum corresponding elements of two lists."""
    list1.extend(list2)
    return sum(list1)

def distinct_and_sorted(input_list):
    """Return a sorted list of distinct elements."""
    return sorted(set(input_list))



length = int(input("Enter length of the rectangle: "))
width = input("Enter width of the rectangle: ")
width = int(width) if width else 10
area = calculate_area(length, width)

print(f"Area of the rectangle: {area}")
print(calculate_factorial(5))
print(reverse_string("hello"))
print(f"sum of lists elements {sum_of_list_element([8,2,3,0,7], [3,-2,5,1])}")
print(f"distinct and sorted list: {distinct_and_sorted([4,1,2,3,3,1,3,4,5,1,7])}")