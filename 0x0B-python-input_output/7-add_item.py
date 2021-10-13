#!/usr/bin/python3
"""
script to add all arguments to a python list
and then save them to a file
"""
from sys import argv
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


file_name = "add_item.json"
try:
    jsonl = load_from_json_file(file_name)
except:
    jsonl = []
for argument in argv[1:]:
    jsonl.append(argument)
save_to_json_file(jsonl, file_name)
