import random
import petname
import json


animalList = ['snake', 'bull' , 'lion', 'raven', 'bunny']

def new_animals():
    head = random.choice(animalList)
    body = gen_body()
    arms = random.randrange(2,11,2)
    legs = random.randrange(3,13,3)
    tails= arms + legs

    new_creature = {
        'head': head,
        'body': body,
        'arms': arms,
        'legs': legs,
        'tails': tails
    }
    return new_creature

def gen_body():
    animal_1 = petname.name()
    animal_2 = petname.name()

    while (animal_1 == animal_2):
        animal2 = petname.name()

    return animal_1 + '-' + animal_2

if __name__ == '__main__':
    creatures = { "animals": [] }

    for i in range(20):
        creatures['animals'].append(animals())

        with open('animals.json', 'w') as out:
            json.dump(creatures, out, indent=2)

