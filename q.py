# import sys
# sys.setrecursionlimit(10**6)  # Increase recursion limit to avoid stack overflow
#
#
# def infinite_recursion():
#     print("This function is running infinitely!")
#     return infinite_recursion()  # Tail call optimization emulation
#
#
# # Call the function to run it infinitely
# infinite_recursion()


# class Trampoline:
#     def __init__(self, func, *args, **kwargs):
#         self.func = func
#         self.args = args
#         self.kwargs = kwargs
#
#     def __call__(self, *args, **kwargs):
#         result, args, kwargs = self.func(*self.args, **self.kwargs)
#         while callable(result):
#             result, args, kwargs = result(*args, **kwargs)
#         print(1)
#         return result
#
#
# # Define the function to be executed infinitely
# def infinite_function(*args, **kwargs):
#     print(f"args: {args}, kwargs: {kwargs}")
#     kwargs['b'] += 1
#     return infinite_function, args, kwargs
#
#
# # Wrap the function with the Trampoline
# infinite_trampoline = Trampoline(infinite_function, 1, a="a", b=1)
#
# # Call the trampolined function
# infinite_trampoline()


# def squares(length):
#     for n in range(length):
#         yield n ** 2

#
# squares = (n**2 for n in range(5))
#
# for square in squares:
#     print(square)
#
#
# # squares = (n**2 for n in range(5))
#
#
# for square in squares:
#     print(square)


from time import sleep

while True:
    try:
        sleep(30)
    except Exception:  # ❌
        pass
