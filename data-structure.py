#Task 3

# Find and print max and min value from a list
nums = [1,2,3,4,5]
print(f"Max value: {max(nums)}")
print(f"Min value: {min(nums)}")

#merge 2 lists and print the merged list
a=[1,2,3,4]
b=[5,6,7,8]
a.extend(b)
print(f"Merged List: {a}")

# Find the occurrence of an element in a list
a = [1,3,4,5,2,1,3,9,3]
print(a.count(3))

# Sort and print the list
a.sort()
print(f"Sorted List: {a}")

# add element in set and print the set
s = {1,2,3,4,5}
s.add(6)
print(s)

# remove element from set and print the set
s.remove(3)
print(s)

# intersection of 2 sets and print the result
s1 = {1,2,3}
s2= {3,4,5}
print(f"Intersection: {s1.intersection(s2)}")

# count the occurrence of element in tuple
fruit = ('apple', 'banana', 'apple', 'cherry')
print(fruit.count('apple'))

# concatenate 2 tuples and print the result
t1 = (1,2,3)
t2 = (4,5,6)
t3 = t1.__add__(t2)
print(f"Concatenated Tuple: {t3}")

# print the value of key from dictionary
person = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(f"Age: {person['age']}")

#remove the key from dictionary and print the dictionary
del person['city']
print(person)

# merge the dictionaries and print the merged dictionary
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict1.update(dict2)
print(f"Merged Dictionary: {dict1}")