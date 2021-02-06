import json
import random

with open('animals.json', 'r') as f:
    animals = json.load(f)
    x = random.randint(0,19)
    print(f"This animals head is {animals['animals'][x]['head']},")
    print(f"has a body of an {animals['animals'][x]['body']},")
    print(f"with {animals['animals'][x]['arms']} arms, ")
    print(f"{animals['animals'][x]['legs']} legs, ")
    print(f"and {animals['animals'][x]['tail']} tails ")
