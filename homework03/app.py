import generate_animals
import random
import json


from flask import Flask, request, abort #the abort function will halt an HTTP error request                                              
app = Flask(__name__)


@app.route('/gen_animals', methods = ['GET'])
def generate_animals():
     # route that pertains to returning the animals                                                                                      
    num_of_animals = request.args.get('num_of_animals')

    if num_of_animals is None: #testing two variables for the same object                                                                
        num_of_animals = 1

    try:
        num_of_animals = int(num_of_animals)
    except ValueError:
        abort(400)
    except:
        abort(400)

    # iterate through list to go through the animals                                                                                     
    creatures = {"animals": [] }
    for n in range(num_of_animals):
        creatures['animals'].append(generate_animals.new_animals() ) #function from generate_animals hw1 appended                        

    with open('animals.json', 'r') as outfile:
        json.dump(creatures, outfile, indent=2)

    return json.dumps(animals, indent=2)

@app.route('/animals', methods = ['GET'])
def retrieve_animals(): #read animals from the file                                                                                      
    try:
        with open('animals.json') as json_file:
            animals = json.load(json_file)
        assert len(animals['animals']) > 0
    except AssertionError:
        abort(404, "Empty Database")
    except FileNotFoundError:
        abort(404, "Database doesn't exist")

    num_of_animals = request.args.get('num_of_animals')

    if num_of_animals is None:
        num_of_animals = 5 #If no animals selected then 5 will be given                                                                  

    try:
        num_of_animals = int(num_of_animals)
        assert num_of_animals <= len(animals['animals'])
        assert num_of_animals > 0
    except AssertionError:
        abort(400, "Has to be within 1 and " + str(len(animals['animals'])))
    except ValueError:
        abort(400, "Variable has to be an int.")
    except:
        abort(400)

    chosen_animals = [] #Selects animals from the list                                                                                   
    for n in range(num_of_animals):
        selected_choice = random.choice(animals['animals'])
        chosen_animals.append(selected_choice)
        animals['animals'].remove(selected_choice) #will delete the animals from the database                                            


    with open('animals.json', 'w') as outfile:
        json.dump(animals, outfile, indent=2)

    return json.dumps(chosen_animals, indent=2)
  
  @app.route('/specify_animals', methods = ['GET'])
def specify_animals():
    try:
        with open('animals.json') as json_file:
            animals = json.load(json_file)
        assert len(animals['animals']) > 0
    except AssertionError:
        abort(404, "Empty Database")
    except FileNotFoundError:
        abort(404, " Database doesn't exist.")

    num_of_animals = request.args.get('num_of_animals')
    head = request.args.get('head_type') # takes the animals head type                                                                   

    if head is not None:
        animals['animals'] = [animal for animal in animals['animals'] if animal['head'] == head]

    if num_of_animals is None:
        num_of_animals = len(animals['animals'])

    try:
        num_of_animals = int(num_of_animals)
        assert num_of_animals <= len(animals['animals'])
        assert num_of_animals > 0
    except AssertionError:
        abort(400, "Has to be within 1 and " + str(len(animals['animals'])) + ", inclusive.")
    except ValueError:
        abort(400, "Variable has to be an int.")

    chosen_animals = []
    for n in range(num_of_animals):
        selected_choice = random.choice(animals['animals'])
        chosen_animals.append(selected_choice)
        animals['animals'].remove(selected_choice)

    return json.dumps(chosen_animals, indent=2)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5014)

