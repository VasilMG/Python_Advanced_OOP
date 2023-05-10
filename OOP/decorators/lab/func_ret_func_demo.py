def manage_list(ll, func):
    return [func(x)for x in ll]

ll = [1, 2, 3]

print(manage_list(ll, lambda x: x + 2))

def f(x):
    def internal_f(y): 
        return x + y
    return internal_f  

f1 = f(2)
print(f1)
print(f1(5)) 
f.new_property = 92 
print(f.new_property) 