#**kwarg accepts any number of keyword arguments(name = value)
# Python collects them into a dictionary
def print_settings(**kwargs):
    
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        
