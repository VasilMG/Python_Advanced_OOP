def age_assignment(*args, **kwargs):
    result = {}
    for item in args:
        if item[0] in kwargs:
            result[item] = kwargs[item[0]]

    the_result = [f"{name} is {age} years old." for name, age in sorted(result.items())]
    return "\n".join(the_result)





print(age_assignment("Amy", "Bill", "Willy", W=36,

A=22, B=61))


#print(age_assignment("Peter", "George", G=26, P=19))