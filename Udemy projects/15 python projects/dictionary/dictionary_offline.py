import json
import os
import sys

# Helper function to find the correct path to the bundled file
def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores the path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Use the resource_path function to locate the JSON file
json_file_path = resource_path("C://Users/USER/Desktop/data.json")

with open(json_file_path) as f:
    data = json.load(f)

def translate(word):
    if word in data:
        return data[word]
    else:
        return "WORD NOT FOUND"

while True:
    word = input("enter your search here: ")
    output = translate(word)
    print(output)
