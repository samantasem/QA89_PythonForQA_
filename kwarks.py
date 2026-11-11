def print_config(**kwargs):
    print(type(kwargs), kwargs)

print_config(browser = "chrome", headless = True, timeout=30)
print_config()