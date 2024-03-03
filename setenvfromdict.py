import sys
import os

# Command line argument: key1:value1,key2:value2
custom_string = sys.argv[1]

# Parse the custom string into a dictionary
my_dict = dict(item.split(":") for item in custom_string.split(","))

print(my_dict)

for key, value in my_dict.items():
    os.environ[key] = value

print(os.environ['key1'])  # Output: value1
print(os.environ['key2'])  # Output: value2