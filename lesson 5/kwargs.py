def print_config(**kwargs):
    print(type(kwargs), kwargs)

print_config(browser = "chrome", headless = True, timeout=30)
print_config()

def create_user(**data):
    return data
user = create_user(name = "Anna",role = "user")
print(user)

#user = create_user("name" : "Kristina")
def example(a,b=10,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
example(1,2,3,6,name="Kristina")