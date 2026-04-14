'''
Understanding Variables and Data Types in Python
==========================
Lesson consists of:
- Variables
- Data types
- Type checking type()
- Type conversion str(), int(), float(), bool()
==========================
'''

name = 'Alice'
print(name, type(name)) # type() is a built-in function in Python that returns the data type of a variable. In this case, it will return <class 'str'>.

is_student = True
print(is_student, type(is_student))

age = 20
print(age, type(age))

score = 80.5
print(isinstance(score, float)) # isInstance() checks if the variable is of a specific data type. It returns True if the variable is of the specified data type, and False otherwise.

'''
OUTPUT:

Alice <class 'str'>
True <class 'bool'>
20 <class 'int'>
True <class 'float'>

'''
