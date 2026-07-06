# We are gonna learn about *args and **kwargs in Python. These are used to pass a variable number of arguments to a function.
def sum_numbers(*args):
    print(f"The sum of the numbers is: {sum(args)}")
sum_numbers(1, 2, 3, 4, 5)  # Output: The sum of the numbers is: 15
def print_info(first,last,**kwargs):
    print(f"First Name: {first}")
    print(f"Last Name: {last}")
    print(f"Additional Info: {kwargs}")
print_info("Rishab","18",age=25,city="New York")

