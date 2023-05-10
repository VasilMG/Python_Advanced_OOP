# namespaces
def  sum1(n):  # Global finctuion in the module
    result = 1 # local for the function or class
    for x in range(n):
        result += x
    return result



print(sum([1, 2, 3])) # Built-in in Python

# scopes
text = ' Hello Gosho'   # Global Scope

def print_greeting():
    text = ' Hello Pesho' # function scope
    print(text)

print(text) # Hello Gosho
print_greeting() # Hello Pesho


def f1():
    text = 'hello f1' # Global
    def f1_inner():    # local for f1_inner
        text = 'hello from inner'
        def f1_innermost():
            text = 'hello f1 innermost'  # local for f1_innermost
            print(text)
        print(text)
        f1_innermost()
    print(text)
    f1_inner()

f1()