import requests
import json
print("Welcome to the qoute generator\n")

apiUrl = "https://api.quotable.io/"

userInput = input("Enter [r] for a random quote or enter [c] to see the categories: ")
print("\n")

if userInput == "r":
    apiUrl += "random"
    response = requests.get(apiUrl)
    if response.status_code == requests.codes.ok:
        x = json.loads(response.text)
        print(x["content"])
    else:
        print("Error:", response.status_code, response.text)
elif userInput == "c":
    apiUrl += 'tags'
    response = requests.get(apiUrl)
    if response.status_code == requests.codes.ok:
        x = json.loads(response.text)
        for data in x:
            print(data["name"])
        userInputCat = input("Enter the full name of one the categories shown: ")
        catApiUrl = f"https://api.quotable.io/random?tags={userInputCat}"
        response = requests.get(catApiUrl)
        if response.status_code == requests.codes.ok:
            x = json.loads(response.text)
            print(x["content"])
        else:
            print("Error:", response.status_code, response.text)
    else:
        print("Error:", response.status_code, response.text)
    
