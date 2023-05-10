

def func_executor(*args):
    functions = {}
    for func_ref, f_values in args:
        f_result = func_ref(*f_values)
        functions[func_ref] = f_result

    return '\n'.join([f"{k.__name__} - {v}" for k,v in functions.items()])

def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2

print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))