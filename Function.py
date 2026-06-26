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
# First-Class Objects
def shout(text):
    return text.upper()
def process_text(func, text):  # Function passed as an argument
    return func(text)
process_text(shout, "hello")  # "HELLO"
# Closures
def multiplier(factor):
    def multiply(number):
        return number * factor  # Remembers 'factor'
    return multiply
triple = multiplier(3)
print(triple(10))  # 30
# Decorators
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper
@my_decorator
def say_wheels():
    print("Wheels up!")
say_wheels()
# Type Hinting (Modern Python)
def calculate_velocity(distance: float, time: float) -> float:
    return distance / time

