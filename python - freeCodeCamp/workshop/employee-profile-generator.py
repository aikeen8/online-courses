'''
Introduction to Strings 
==========================
Lesson consists of:
- String concatenation + operator, f-strings
- String slicing [start:end], negative indices
==========================
'''

first_name = 'John'
last_name = 'Doe'
full_name = first_name + ' ' + last_name # The + operator is used to concatenate (combine) strings in Python.
address = '123 Main Street'
address += ', Apartment 4B' # The += operator is a shorthand for concatenating and assigning a new value to the variable. Saves you time from writing the variable name twice.

employee_age = 28

employee_info = full_name + ' is ' + str(employee_age) + ' years old' # str() is a built-in function in Python that converts a value to a string. It will throw an error if you try to concatenate a string with a non-string value without converting it first. 

experience_years = 5
experience_info = 'Experience: ' + str(experience_years) + ' years'
print(experience_info)

'''
OUTPUT:
John Doe is 28 years old
Experience: 5 years
'''


position = 'Data Analyst'
salary = 75000

employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}' # f-strings (formatted string literals) are a way to embed expressions inside string literals, using curly braces {}. An alternative for concatenating strings with + operators and str() function.
print(employee_card)

employee_code = 'DEV-2026-JD-001'

# String slicing allows you to extract a portion of a string by specifying the start and end indices. The syntax is string[start:end], where start is the index of the first character you want to include, and end is the index of the first character you want to exclude. 
department = employee_code[0:3]
print(department)
year_code = employee_code[4:8]
print(year_code)
initials = employee_code[9:11]
print(initials)
last_three = employee_code[-3:] # You can also use negative indices to slice from the end of the string. -1 is the last character, -2 is the second to last character, and so on. 
print(last_three )

'''
OUTPUT:
Employee: John Doe | Age: 28 | Position: Data Analyst | Salary: $75000
DEV
2026
JD
001
'''