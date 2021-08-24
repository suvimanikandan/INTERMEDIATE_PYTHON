
# f-Strings
# New since Python 3.6. Use the variables directly inside the braces.


name = "Eric"
age = 25
a = f"Hello, {name}. You are {age}."
print(a)
pi = 3.14159
a = f"Pi is {pi:.3f}"
print(a)
# f-Strings are evaluated at runtime, which allows expressions
a = f"The value is {2*60}"
print(a)