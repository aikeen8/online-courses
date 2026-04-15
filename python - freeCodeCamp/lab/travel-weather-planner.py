'''
Booleans and Conditionals 
==========================
Lesson consists of:
- Comparison operators: ==, !=, >, <, >=, <=
- Logical operators: and, or, not
- if, elif, else statements
==========================
'''

# create the following variables with the given values
distance_mi = 120
is_raining = False
has_bike = True
has_car = False
has_ride_share_app = True

# if distance_mi is a falsy value, print False
if distance_mi == 0:
    print(False)

# you should use if, elif, and else statements to evaluate the distance categories in ascending order.
# If the distance is less than or equal to 1 mile and if it is not raining, print True. Otherwise, print False.
elif distance_mi <= 1:
    if not is_raining:
        print(True)
    else:
        print(False)
# If the distance is greater than 1 mile and less than or equal to 6 miles and only if the user has a bike and it is not raining, print True. Otherwise, print False.
elif distance_mi > 1 and distance_mi <= 6:
    if has_bike and not is_raining:
        print(True)
    else:
        print(False)
# If the distance is greater than 6 miles and if the user has a car or has a ride share app, print True. Otherwise, print False.
elif distance_mi > 6:
    if has_car or has_ride_share_app:
        print(True)
    else:
        print(False)

'''
OUTPUT:
True
'''