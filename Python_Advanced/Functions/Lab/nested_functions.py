def greeting(name):
    hello = 'Hello, '
    def say_hi(last_name):
        return hello + name +' ' + last_name
    return say_hi # mnogo vajno da e BEZ skobi!!!!

f2 = greeting(name="Gosho")

print(f2('Petrov'))


# def math_operation(operation):
#     def add(*args):
#         return sum(args)
#     def subtract(*args):
#         return sum(-args)
#     def multyply(*args):
#         result = 1
#         for x in args:
#             result *= x
#         return result
#
#     if operation == "+":
#         return add
#     elif operation == "-":
#         return subtract
#     elif operation == "*":
#         return multyply
#     else:
#         return None
# # returns the function and we can use it in the code.. outside the first function
