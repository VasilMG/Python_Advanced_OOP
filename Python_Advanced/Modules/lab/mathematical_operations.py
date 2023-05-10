def perform_operation(sing, * args):
    if sing == '+':
        return sum(args)
    if sing == '-':
        result = args[0]
        for x in args[1:len(args)]:
            result -= x
        return result

    if sing == '*':
        result = 1
        for x in args:
            result *= x
        return result

    if sing == '/':
        result = args[0]
        for x in args[1:len(args)]:
            result /= x

        return result

