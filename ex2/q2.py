def wrap(func1):
    def wrapper():
        print("inner wrap")
        func1()
        print("end of wrap")
    return wrapper
    
@wrap
def f(x):
    print(x**2)

f()

# def wrap(func):
#     def wrapper():
#         print(f"starting {func.__name__}")
#         func()
#         print(f"ending {func.__name__}")
#     return wrapper

# @wrap
# def a_function():
#     print("I'm a new function")

# a_function()