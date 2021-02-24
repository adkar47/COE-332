
import json
import random
import sys

def error_message(error_text):
    print("[error] read_animals.py: " + error_text)
    sys.exit(1)

def obtain_num_animals(args, max_number):
    num_of_animals = int(args)

    assert num_of_animals >= 1
    assert num_of_animals <= max_number

    return num_of_animals

if __name__ == '__main__':


    with open('animals.json', 'r') as f:
        animals = json.load(f)

    try:
        num_of_animals = obtain_num_animals(sys.argv[1], len(animals['animals']))

    except AssertionError:
        error_message("\'num_of_animals\' should stay within the range 1 to " + str(len(animals['animals'])) + ", inclusive.")
    except ValueError:
        error_message("\'num_of_animals\' should be an integer")
    except IndexError:
        error_message("read_animals.py should have a parameter \'num_of_animals\'.")

    animals_list = []
    for n in range(num_of_animals):
        new_selection = random.choice(animals['animals'])
        animals_list.append(new_selection)
        animals['animals'].remove(new_selection)

    print(json.dumps(animals_list, indent=2))
