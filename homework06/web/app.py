from flask import Flask, request
import json
import petname
import json
import uuid
import redis
import random
import datetime

app = Flask(__name__)
rd = redis.StrictRedis(host='10.97.21.171', port=6379, db=0)

#returns animals based on UUID                                                                                                                                                                                                                                                                                                                         \
                                                                                                                                                                                                                                                                                                                                                        
@app.route('/animals_uuid', methods= ['GET'])
def get_animal_uuid():
     animals = {}
     count = 1
     for key in rd.keys():
         animals[str(count)] = str(key)
         count += 1

     return json.dumps(animals)

#returns animals in the database                                                                                                                                                                                                                                                                                                                       \
                                                                                                                                                                                                                                                                                                                                                        
@app.route('/get_animals', methods= ['GET'])
def obtain_animals():
     animals = []
     for key in rd.keys():
         animals.append(json.loads(rd.get(key).decode('utf-8')))


     return json.dumps(animals)

#selects a creature based on its uuid                                                                                                                                                                                                                                                                                                                  \
                                                                                                                                                                                                                                                                                                                                                        
@app.route('/unique_uuid/', methods= ['GET'])
def get_ani():
     unique_Id = request.args.get('uuid')
     return json.dumps(json.loads(rd.get(unique_Id).decode('utf-8')))

#displays the number of animals in the database                                                                                                                                                                                                                                                                                                        \
                                                                                                                                                                                                                                                                                                                                                        
@app.route('/total', methods= ['GET'])
def get_total():
     return str(len(rd.keys()))


#returns average number of legs per animal                                                                                                                                                                                                                                                                                                             \
                                                                                                                                                                                                                                                                                                                                                        
@app.route('/get_num_of_legs', methods= ['GET'])
def get_legs():
     animals = []
     avg_num_of_legs = 0

     for key in rd.keys():
         animals.append(json.loads(rd.get(key).decode('utf-8')))

     for animal in animals:
         avg_num_of_legs += int(animal['legs'])

     return str(avg_num_of_legs / 20.0)

#deletes a section of data on date range                                                                                                                                                                                                                                                                                                               \
                                                                                                                                                                                                                                                                                                                                                        
@app.route('/clear', methods= ['GET'])
def delete_database():

    rd.flushdb()


    for i in range(20):

        start_date = datetime.date(2001, 7, 24)
        end_date = datetime.date(2021, 7, 24)
        difference = end_date - start_date
        days_between = difference.days
        random_num_days = random.randrange(days_between)

        my_animal = {}
        unique_Id = str(uuid.uuid4())
        my_animal['head'] = random.choice(['snake', 'bull', 'lion', 'raven', 'bunny'])
        my_animal['body'] = petname.name() + '-' + petname.name()
        my_animal['arms'] = random.randint(1,5) * 2
        my_animal['legs'] = random.randint(1,4) * 3
        my_animal['tail'] = my_animal['legs'] + my_animal['arms']
        my_animal['created: '] = str(start_date + datetime.timedelta(days=random_num_days))


        rd.set(unique_Id, json.dumps(my_animal))

    return 'Success'

#edits a creature based on uuid                                                                                                                                                                                                                                                                                                                        \
                                                                                                                                                                                                                                                                                                                                                        
@app.route('/edit_uuid/', methods= ['GET'])
def edit_uuid():
     unique_Id = request.args.get('uuid')
     parameter = request.args
     animal = json.loads(rd.get(unique_Id).decode('utf-8'))

     for key in parameter:

         if key == 'uuid':
             continue

         animal[key] = parameter[key]


     rd.set(unique_Id, json.dumps(animal))
     return json.dumps(animal)

# return  animals created between a range of dates                                                                                                                                                                                                                                                                                                     \
                                                                                                                                                                                                                                                                                                                                                        
@app.route('/query/', methods= ['GET'])
def get_animal():
     beginning_date = datetime.datetime.strptime(request.args.get('beginningDate'), '%Y-%m-%d')
     end_date = datetime.datetime.strptime(request.args.get('endDate'),'%Y-%m-%d')
     animals = []
     date_of_animal = []


     for key in rd.keys():
         animals.append(json.loads(rd.get(key).decode('utf-8')))


     for animal in animals:
         date_created = datetime.datetime.strptime(animal['created: '])
         if (date_created >= beginning_date) and (date_created <= end_date):
             date_of_animal.append(animal)

     return json.dumps(date_of_animal)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
