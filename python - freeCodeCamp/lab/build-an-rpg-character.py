# 1. You should have a function named create_character. 
# 2. The function should accept, in order, a character name followed by three stats: strength, intelligence, and charisma.
def create_character(name, strength, intelligence, charisma):

# 3. The character name should be validated: 
    # If the character name is not a string, the function should return The character name should be a string
    if not isinstance(name, str):
        return "The character name should be a string"
    # If the character name is an empty string, the function should return The character should have a name
    if name == "":
        return "The character should have a name"
    # If the character name is longer than 10 characters, the function should return The character name is too long
    if len(name) > 10:
        return "The character name is too long"
    # If the character name contains spaces, the function should return The character name should not contain spaces
    if " " in name:
        return "The character name should not contain spaces"
    
# 4. The stats should also be validated:
    # If one or more stats are not integers, the function should return All stats should be integers
    if not all(isinstance(stat, int) for stat in [strength, intelligence, charisma]):
        return "All stats should be integers"
    # If one or more stats are less than 1, the function should return All stats should be no less than 1
    if any(stat < 1 for stat in [strength, intelligence, charisma]):
        return "All stats should be no less than 1"
    # if one or more stats are greater than 4, the function should return All stats should be no more than 4
    if any(stat > 4 for stat in [strength, intelligence, charisma]):
        return "All stats should be no more than 4"
    # If the sum of all stats is different than 7, the function should return The character should start with 7 points
    if sum([strength, intelligence, charisma]) != 7:
        return "The character should start with 7 points"
    
# 5. If all values pass the verification, the function should return a string with four lines:
    # the first line should contain the character name
    # lines 2-4 should start with the stat abbreviation, STR, INT or CHA (in this order), then a space, and then a number of full dots (●) equal to the value of the stat, and a number of empty dots (○) to reach 10. Example: if the value of strength is 3 there must be 3 full dots followed by 7 empty dots. The dots are given in the editor.
    # Here's the string that should be returned by create_character('ren', 4, 2, 1):
    # ren
    # STR ●●●●○○○○○○
    # INT ●●○○○○○○○○
    # CHA ●○○○○○○○○○
    return f"{name}\nSTR {'●' * strength}{'○' * (10 - strength)}\nINT {'●' * intelligence}{'○' * (10 - intelligence)}\nCHA {'●' * charisma}{'○' * (10 - charisma)}"

