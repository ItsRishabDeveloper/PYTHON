def age():
    a = 10
    return a
    # This variable 'a' is local to the function 'age' and cannot be accessed outside of it.
b = 20
# Note that the variable 'b' is defined outside of any function, making it a global variable. It can be accessed from anywhere in the code, including inside functions, unless shadowed by a local variable with the same name.
print(b)
print(age())  # This will raise an error because 'a' is not defined in the global scope.