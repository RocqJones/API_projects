import requests
from random import choice
#choice is a method that picks values from a list and return them randomly
import pyfiglet
from termcolor import colored

header = pyfiglet.figlet_format("ROCQJONES JOKES")
header = colored(header, color="blue")
print(header)

user_input = input("What would like to search for? ")
url = "https://icanhazdadjoke.com/search"

response = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term": user_input}
).json() #it is the same as creating a variable name for .json() method
#res_json = response.json()

num_jokes = len(response["results"])
num_jokes == response["total_jokes"] #total_jokes is returned by the json code generated as dict
results = response["results"]
if num_jokes > 1:
    print(f"I found {num_jokes} jokes about {user_input}. Here we go!!!")
    print(choice(results) ['joke'])
elif num_jokes == 1:

    print("THERE IS ONLY ONE JOKE!!!")
    print(results [0] ['joke'])
else:
    print(f"SORRY, THERE ARE NO JOKES. Try again {user_input}")