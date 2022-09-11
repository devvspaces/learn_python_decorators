"""
Learn python decorators
"""


# def split_string(func):
#     def inner(*args, **kwargs):
#         return func(*args, **kwargs).split()
#     return inner


# def uppercase_string(func):
#     def inner(*args, **kwargs):
#         return func(*args, **kwargs).upper()
#     return inner


# @split_string
# @uppercase_string
# def speak_language(word, language):
#     return f"I {word} speaking {language}"


# print(speak_language("hate", "Python"))


# def apply_increase(increase):

#     def increase_number(func):

#         def wrapper():
#             return func() + increase

#         return wrapper

#     return increase_number


# @apply_increase(10)
# def calculate_number():
#     return 5


# @apply_increase(1)
# def myother_number():
#     return 1


# print(calculate_number())
# print(myother_number())


# def A(arg1):
#     def B():
#         def C():
#             def D():
#                 def E():
#                     print(arg1)
#                 return E
#             return D
#         return C
#     return B


# A("Good Python")()()()()

# Decorator to increase function output by one
# def increase_number(func):

#     def wrapper():
#         return func() + 1

#     return wrapper


# def calculate_number():
#     return 5


# var_a = increase_number(calculate_number)
# inner_function_response = var_a()
# print(inner_function_response)


# def outer_function(func):

#     print("Before defining inner function")

#     def inner_function():

#         print("Do something before calling function")

#         func()  # Call function passed as argument in outer function

#         print("Do something after calling function")

#     print("Do something before returning the inner function")

#     return inner_function


# def sample():
#     print("I was decorated")


# outer_function(sample)()



