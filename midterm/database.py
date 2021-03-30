import json
import redis
import uuid
from dateutil import parser
import generate_animals
import datetime

REDIS_HOST = 'redis'
REDIS_PORT = 6379

def sum_animals(num):
    rd = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, database=0)

    for n in range(num):
        unique_Id = str(uuid.uuid4())
        animals = generate_animals.new_animals()

        rd.set(unique_Id , json.dumps(animals))


# clears all entires from the database                                                                                                                                                                                               
def delete_animals():
    rd = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, database=0)
    redis_keys = [key.decode('utf-8') for key in rd.keys()]

    for key in redis_keys:
        rd.delete(key)


# returns a dict containing all animals in the format { 'uuid': {traits} , ... }                                                                                                                                                     
def get_animals():
    rd = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, database=0)
    redis_keys = [key.decode('utf-8') for key in rd.keys()]

    animals = {}
    for key in redis_keys:
        animals[key] = json.loads(rd.get(key).decode('utf-8'))

    return animals


# returns a dict with the animals created within the given start and end dates                                                                                                                                                       
def query_dates(start, end):
    animals = get_animals()

    start_date = parser.parse(start)
    end_date = parser.parse(end)

    assert start_date <= end_date

    choosen_animals = {}
    for key in animals.keys():
        current_date = parser.parse( animals[key]['created_on'] )
        if start_date <= current_date <= end_date:
            choosen_animals[key] = animals[key]
        else:
            pass

    return selected_animals

# returns a dict containing the animal with a specified uuid                                                                                                                                                                         
def get_creature_by_uuid(unique):
    rd = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, database=0)
    features = json.loads( rd.get(unique).decode('utf-8') )
    return { unique: features }


# traits of animals are edited based on the UUID                                                                                                                                                                                     
def edit_creature_by_uuid(unique, new_traits):
    rd = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, database=0)
    features = json.loads( rd.get(unique).decode('utf-8') )

    for key in new_feautures.keys():
        features[key] = new_features[key]

    rd.delete(unique)
    rd.set(unique, json.dumps(features))


# deletes the animals from the database in between the given dates                                                                                                                                                                   
def delete_date_range(start, end):
    rd = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, database=0)

    animals = get_animals()

    start_date = parser.parse(start)
    end_date = parser.parse(end)

    assert start_date <= end_date

    selected_animals = []
    for key in animals.keys():
        this_date = parser.parse(animals[key]['created_on'])
        if start_date <= this_date <= end_date:
            rd.delete(key)
        else:
            pass


# returns average of legs for animals in the database                                                                                                                                                                                
def get_average_num_of_legs():
    rd = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, database=0)
    redis_keys = [key.decode('utf-8') for key in rd.keys()]

    animals = get_animals()

    total_legs = 0
    for key in redis_keys:
        total_legs = total_legs + animals[key]['legs']

    average_legs = total_legs/count_animals()
    return average_legs



# returns a total count of animals in the database                                                                                                                                                                                   
def total_count():
    rd = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0)
    return len( [key.decode('utf-8') for key in rd.keys()] )
