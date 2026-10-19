def show_info(name,age):
    print(f"{name} is {age} years old")
    
    
person = ("Bob", 37)
# * is unpacking the tuple into separate positional arguments
# equivalent to show_info("Bob", 37)
show_info(*person)

person = {"name": "Bob", "age": 25}
#** unpacks the dictionary into keyword arguments
# equivalent to show_info(name = "Bob", age = 25)
show_info(**person)

def print_deliviery(customer,city,parcels):
    print(f"{customer} has {parcels} parcels going to {city}.")
    
delivery = ("Maya", "Edmonton", 3)
print_deliviery(*delivery)