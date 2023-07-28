
def generate(length,
             lower: bool = None,
             upper: bool = None,
             symbols: bool = None,
             numbers: bool = None) -> str:
    import random 
    #list of characters
    Lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x','y', 'z']

    Upper = [e.capitalize() for e in Lower]

    Symbols = ['!', '$', '%', '&','*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?',
            '@', '\\', '^', '_', '`', '|', '~']

    Numbers = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']

   
    ls = []
    result = ''
 
    ls += Lower if lower else []
    ls += Upper if upper else []
    ls += Symbols if symbols else []
    ls += Numbers if numbers else []

    if len(ls) == 0:
        return 'You need to atleast choose one option'
    
    result = ''.join(random.choices(''.join(ls), k=length))
    return result


def checker(password):
    """
    Verify the strength of 'password'
    Returns a dict indicating the wrong criteria
    A password is considered strong if:
        8 characters length or more
        1 digit or more
        1 symbol or more
        1 uppercase letter or more
        1 lowercase letter or more
    """


    length = len(password) > 8
    digits = False
    uppercase = False
    lowercase = False
    symbol = False 

    if any(char.isdigit() for char in password):
        digits = True

    if any(char.isupper() for char in password):
        uppercase = True
    
    if any(char.islower() for char in password):
        lowercase = True
    
    if any(not char.isalnum() for char in password):
        symbol = True

    # overall result
    password = not(length or digits or uppercase or lowercase or symbol )

    return length, digits, uppercase, lowercase, symbol 

print(list(checker("3eqfZk,G|;<KZo-k")))
#print(f'{lower = }')
#print(f'{upper = }')

