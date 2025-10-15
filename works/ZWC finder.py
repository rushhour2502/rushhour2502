import re


text = input("Enter a text to check for ZWC: ")
pattern = r'[\u200B\u200C\u200D\u200E\u200F\uFEFF]'
matches = re.findall(pattern, text)

if matches:
    print("ZWC found", matches)
else:
    print("ZWC not found")