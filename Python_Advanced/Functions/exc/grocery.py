def grocery_store(**kwargs):
    dd = {}
    #ll = sorted(kwargs.items(), key= lambda x:(-x[1], -len(x[0]), x[0]))
    ll = [f"{k}: {v}" for k, v in sorted(kwargs.items(), key= lambda x:(-x[1], -len(x[0]), x[0]))]

    return '\n'.join(ll)


print(grocery_store(

bread=5,

pasta=12,

eggs=12,

))

print(grocery_store(

bread=2,

pasta=2,

eggs=20,

carrot=1,

))