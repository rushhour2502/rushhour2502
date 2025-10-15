# libraries
import requests
import json
from difflib import get_close_matches

# # for url located data
# url = "https://drive.google.com/uc?export=download&id=1Uyb9_G6rZ0GwXBw9wLs4D51zcp0kYtzU"
# response = requests.get(url)
# if response.status_code==200:
#    data = response.json()
# else:
#    print(f"ERROR! COULD NOT RETRIEVE DATA. status code: {response.status_code}")

# # for local data
data= json.load(open("C:/Users/USER/Desktop/pypros/Udemy projects/15 python projects/data.json"))

def translate(word):
    word= word.lower()

    if word in data:
        return data[word]
    
    elif word.title() in data:
        return data[word.title()]
    
    elif word.upper() in data:
        return data[word.upper()]


    # to suggest close matches
    elif len(get_close_matches(word, data.keys()) )>0:
        suggestion = get_close_matches(word, data.keys())[0]
        print(f"did you mean: {suggestion}?")

        while True:
            decide = input("Enter y if this is what you mean or n if not: ").lower().strip()
            if decide == "y":
                return data[suggestion]
            elif decide=="n":
                print ("Okay, try searching for another word")
                break
            else:
                print("Invalid input, please enter 'y' or 'n'.")
    else:
       return "WORD NOT FOUND"

while True:
    word = input("enter your search here: ").strip()
    
    #check if word input is empty
    if word:
        output = translate(word) 
        
        if type(output)==list:
            for item in output:
                print (item)
        else:
            print(output)   
    else:
        print("please enter a valid word")

    





   