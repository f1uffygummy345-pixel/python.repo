def show_info(name,age):
    print(f"{name} is {age} years old")
    
    
person = ("Bob", 37)
# * is unpacking the tuple into separate positional arguments
# equivalent to show_person("Bob", 37)
show_info(*person)