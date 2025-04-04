def show_fubctiob_name(func):
    def function_name(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        return result
    return function_name
@show_fubctiob_name 
def greet(name):
    print(f"Hello, {name}!")
@show_fubctiob_name
def square(num):
    print(f"Square of {num} is {num ** 2}")

greet("Alice")
square(4)