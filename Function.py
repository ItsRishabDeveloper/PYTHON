def greet(name):
    """This function greets the person passed in as a parameter."""
    print("Hello, " + name + ". Good morning!")
# Parameter Mechanics (The 5 Types)
# A. Positional Arguments
def divide(a,b):
    return a / b
# B. Keyword Arguments
def add(a=5,b=7):
    return a + b
# C. Default Parameters
def sub(a,b):
    return a - b
# D. Variable-Length Arguments (*args and kwargs)
def master_function(*args, **kwargs):
    print(args)    # e.g., (1, 2, 3)
    print(kwargs)  # e.g., {'key': 'value'}
# E. Positional-Only and Keyword-Only Enforcers
def strict_function(pos_only, /, positional_or_keyword, *, kw_only):
    pass
# valid call:
strict_function(1, 2, kw_only=3)
# invalid call (raises TypeError):
strict_function(pos_only=1, positional_or_keyword=2, kw_only=3)
divide(10, 2) # Output: 5.0
add() # Output: 30
sub()
master_function(1, 2, 3, key='value') # Output: (1, 2, 3) {'key': 'value'}
strict_function(1, 2, kw_only=3) # valid call

# Lambda Functions
square = lambda x: x ** 2
print(square(4))  # 16

