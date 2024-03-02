import json
import os
import sys

print (sys.argv[1]) 



# # Path to the JSON file
# json_file_path = 'input.json'

# # Read JSON file
# with open(json_file_path, 'r') as file:
#     json_data = json.load(file)

# # # Print key-value pairs
# # for key, value in json_data.items():
# #     print(f"Key: {key}, Value: {value}")

# # Set each key as environment variable
# for key, value in json_data.items():
#     os.environ[key] = str(value)

# # Print environment variables
# for key, value in os.environ.items():
#     print(f"Environment Variable: {key}, Value: {value}")