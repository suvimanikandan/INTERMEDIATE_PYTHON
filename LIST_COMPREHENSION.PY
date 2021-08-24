# List comprehension
# A elegant and fast way to create a new list from an existing list.

# List comprehension consists of an expression followed by a for statement inside square brackets.


a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [i * i for i in a] # squares each element
print(b)