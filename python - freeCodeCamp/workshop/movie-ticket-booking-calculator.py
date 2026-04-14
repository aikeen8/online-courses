'''
Booleans and Conditionals 
==========================
Lesson consists of:
- Comparison operators: ==, !=, >, <, >=, <=
- Logical operators: and, or, not
- if, elif, else statements
- Nested conditionals
==========================
'''

base_price = 15
age = 21
seat_type = 'Gold'
show_time = 'Evening'

if age > 17:
    print('User is eligible to book a ticket')

if age >= 21:
    print('User is eligible for Evening shows')
else:
    print('User is not eligible for Evening shows')

'''
OUTPUT:
User is eligible to book a ticket
User is eligible for Evening shows
'''

is_member = False
is_weekend = False

discount = 0
if is_member and age >= 21: # The condition checks if the user is a member and is 21 years or older. If BOTH conditions are TRUE, the user qualifies for a membership discount.
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print('Discount:', discount)

'''
OUTPUT:
User does not qualify for membership discount
Discount: 0
'''

extra_charges = 0
if is_weekend or show_time == 'Evening': # The condition checks if it is a weekend OR if the show time is in the evening. If EITHER condition is TRUE, extra charges will be applied.
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')
print('Extra charges:', extra_charges)

'''
OUTPUT:
No extra charges will be applied
Extra charges: 0
'''

if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member): # The condition checks if the user is 21 years or older OR if the user is 18 years or older AND (the show time is NOT in the evening OR the user is a member). If ANY of these conditions are TRUE, the ticket booking condition is satisfied.
    print('Ticket booking condition satisfied')

    service_charges = 0
    if seat_type == 'Premium': # nested condition checks the type of seat.
        service_charges = 5
    elif seat_type == 'Gold': 
        service_charges = 3
    else:
        service_charges = 1
    print('Service charges:', service_charges)  
else:
    print('Ticket booking failed due to restrictions')

'''
OUTPUT:
Ticket booking condition satisfied
Service charges: 3
'''