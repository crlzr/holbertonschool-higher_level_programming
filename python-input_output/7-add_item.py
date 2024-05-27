#!/usr/bin/python3
"""
A script that adds all argument to a python list
and save them to a file
"""
import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
filename = "add_item.json"

# Try to load the existing list from the file, or create a new list if the file doesn't exist
if os.path.exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Add all command-line arguments to the list (excluding the script name itself)
items.extend(sys.argv[1:])

# Save the updated list to the file
save_to_json_file(items, filename)
