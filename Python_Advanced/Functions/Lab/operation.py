def operate(operation, *args):
    def add(*args):
        return sum(x for x in args)

    def subtract(x,*args):
        return x + sum( -y for y in args)

    def multyply(*args):
        result = 1
        for x in args:
            result *= x

        return result
    def divide(x,*args):
        result = x
        for l in args:
            result /= l
        return result

    if operation == "+":
        return add(*args)
    elif operation == "-":
        return subtract(*args)
    elif operation == "*":
        return multyply(*args)
    elif operation == "/":
        return divide(*args)
    else:
        return None


