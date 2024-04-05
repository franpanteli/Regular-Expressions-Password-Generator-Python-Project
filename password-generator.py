"""
    -> We are defining a function, `generate_password` to create a random password 
    -> A password random generation function 
    -> The arguments of this function are the length of the random password we want to generate, 
        and the numbers of numeric, special, uppercase and lowercase characters we want it to have 

    -> Then we import its modules: 
        -> re <- Regular expressions 
        -> secrets <- For secure random number generation 
        -> string <- For string constants 

    -> We are then defining three sets of characters and combining them: 
        -> letters <- For lowercase and uppercase letters 
        -> digits <- For numeric characters 
        -> symbols <- For special characters 
        -> Then combining all three of these into all_characters 

    -> Then using a while loop to generate a password:
        -> We have a set of constraints, which are provided by the input parameters (the function arguments) 
        -> We take these, and iterate through different potential passwords in a while loop, until we 
            find one which satisfies all of the conditions which the input parameters specify it
            should have 
        -> We are using the arrays which we just initialised to do this 
        -> I.e we first import the modules, then define the function with various arguments, initialise arrays 
            -> and are now using these in a while loop
        -> In this loop, we are adding random characters from `all_characters` to the `password` string 

    -> The password for this which we want to generate must follow given constraints:
        -> These are inputted in as arguments 
        -> And then we are storing them in a list of tuples 
        -> A constraint being a number of characters and a regular expression pattern to match it 

    -> We then want to check if the generated password matches the constraints, by using an `all` function: 
        -> If the password meets all the constraints, then it is returned 
        -> Then if we are in the main .py file for the project (if the current .py file isn't defining a module and 
            it's the main .py file in the project), then test the function 
            -> In other words, generate a password with the default parameters to test the function 
            -> We are counting the occurrences of specific character types in the generated password, by using the 
                regular expressions in the constraints 
"""

# Import modules 
import re
import secrets
import string

def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    # Define the possible characters for the password
        # All letters
    letters = string.ascii_letters
        # All digits
    digits = string.digits
        # All punctuation
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:

        # Build out the random password, until the constraints we want it to satisfy are met
        password = ''

        # Generate a random password
        for _ in range(length):
            password += secrets.choice(all_characters)
        constraints = [

            # We are using tuples to achieve this (refer to the project problem-solving thought process notes for 
                # more detail on this)
            (nums, r'\d'),
            (lowercase, r'[a-z]'),
            (uppercase, r'[A-Z]'),
            (special_chars, fr'[{symbols}]')
        ]        

        # Check constraints
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            return password
        
# Test the function we just defined, if this .py file is the main one for the project (not one 
    # which is for defining modules)

if __name__=='__main__' :
    new_password = generate_password()
    print('Generated Password:', new_password)


