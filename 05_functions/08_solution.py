def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="sahin", power="smart")
print_kwargs(name="sachin")