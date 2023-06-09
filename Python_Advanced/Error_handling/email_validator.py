class NameTooShort(Exception):
    pass
class MustContainAtSymbolError(Exception):
    pass
class InvalidDomainError(Exception):
    pass

valid_domains = ("com", "bg", "org", "net")

def valid_email(email):
    try:
        name, domain = email.split("@")
    except ValueError:
        raise MustContainAtSymbolError("Email must contain @")
    try:
        name, extension = domain.split(".")
    except ValueError:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    if extension not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    if len(name) < 4:
        raise NameTooShort("Name must be more than 4 characters")
    return True


while True:
    email = input()
    if valid_email(email):
        print("Email is valid")