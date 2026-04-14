'''
Numbers and Mathematical Operations
==========================
Lesson consists of:
- Numbers (integers and floats)
- Mathematical operations: +, -, *, /, //, %, **, parentheses
- Augmented assignment operators: +=, -=, *=, /=, //=, %=,
- round() function
==========================
'''

running_total = 0
num_of_friends = 4

appetizers = 37.89
main_courses = 57.34
desserts = 39.39
drinks = 64.21

running_total += appetizers + main_courses + desserts + drinks # The += operator is a shorthand for adding a value to the existing value of the variable.
print('Total bill so far:', running_total)

tip = running_total * 0.25
print('Tip amount:', tip)

running_total += tip
print('Total with tip:', running_total)

final_bill = running_total / num_of_friends
print('Bill per person:', final_bill)

each_pays = round(final_bill, 2) # The round() function is a built-in function in Python that rounds a number to a specified number of decimal places.
'''
OUTPUT:
Total bill so far: 199.83
Tip amount: 49.9575
Total with tip: 249.7875
Bill per person: 62.446875
Each person pays: 62.45
'''