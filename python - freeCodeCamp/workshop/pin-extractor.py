'''
Loops and Sequences
==========================
Lesson consists of:
- for loops
- def keyword
- split() method
- enumerate() function
- append() method
- list indexing
==========================
'''

def pin_extractor(poems): 
    secret_codes = [] # The function pin_extractor takes a list of poems as input and initializes an empty list called secret_codes to store the extracted secret codes.
    for poem in poems: # The function iterates through each poem in the input list using a for loop. For each poem, it initializes an empty string secret_code to build the secret code for that poem.
        secret_code = ''
        lines = poem.split('\n') # The split() method is used to split the poem into lines based on the newline character ('\n'), resulting in a list of lines.
        for line_index, line in enumerate(lines): # The enumerate() function is used to iterate through the lines of the poem, providing both the line index (line_index) and the line content (line) in each iteration.
            words = line.split()
            if len(words) > line_index: # If the number of words in the line is greater than the line index, it means there is a word at the position corresponding to the line index. 
                secret_code += str(len(words[line_index]))
            else:
                secret_code += '0'
        secret_codes.append(secret_code) # After processing all lines of the poem, the constructed secret code for that poem is appended to the secret_codes list using the append() method.
    return secret_codes

poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

poem2 = 'The grass is green\nhere and there\nhoping for rain\nbefore it turns yellow'
poem3 = 'There\nonce\nwas\na\ndragon'

print(pin_extractor([poem, poem2, poem3]))