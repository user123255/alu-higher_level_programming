#!/usr/bin/python3
"""Script that adds all arguments to a Python list and saves them to a file."""

import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Load existing items if the file exists, else start with empty list
if os.path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Add new command line arguments
my_list.extend(sys.argv[1:])

# Save updated list to file
save_to_json_file(my_list, filename)
