def get_info(name, town, age):
    return f"This is {name} from {town} and he is {age} years old"


dd1 = {"name": "George", "town": "Sofia", "age": 20}

print(get_info(**dd1))
