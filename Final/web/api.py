import json
from flask import Flask, request
import jobs
from jobs import q, rd_jobs , rd_data
import uuid
import requests
import pandas as pd
import redis
import os
import datetime

#Tester route                                                                                                                                                                                                                           
app = Flask(__name__) #Uses the json file to fill the database with animal intake data                                                                                                                                                  
@app.route('/populate', methods=['POST'])
def data():
    with open("Animal_Center.json", "r") as f:
         animal_intake = json.load(f)

    for item in animal_intake:
        rd_data.hmset(item['animal_id'],item)

#Need to create 4 different flask routes                                                                                                                                                                                                
#C : /Insert                                                                                                                                                                                                                            
#R : /Obtain_Intake                                                                                                                                                                                                                     
#U : /Update                                                                                                                                                                                                                            
#D : /terminate                                                                                                                                                                                                                         

@app.route('/Insert', methods = ['GET','POST'])
def Insert():
    try:
        insert = request.get_json(force=True)
    except Exception as f:
        return True, json.dumps({'status': "Error", 'message': 'Invalid JSON: {}.'.format(f)})

    dataframe = get_data()
    dataframe['intakes'].append(add)
    rd_data.set('key', json.dumps(dataframe))

    return json.dumps(get_data, indent = 4)


@app.route('/Obtain_Intake', methods=['GET'])
def obtain_Animal():
#   animal_id = request.args.get('Animal_ID')                                                                                                                                                                                           
#   return json.dumps(rd_data.hgetall(animal_id), indent=4)                                                                                                                                                                             

    dataframe = jobs.get_data()
    result= {}
    animal_id = request.args.get('Animal_ID')
    for i in dataframe['new intake']:
        if i['Animal ID'] == animal_id:
            output = i

    return json.dumps(result, indent = 4)

@app.route('/Update/', methods=['GET'])
def Update():
    dataframe =jobs.get_data()

    animal_id = request.args.get('Animal_ID')
    intake_type = request.args.get('intaketype')
    intake_condition = request.args.get('intakecondition')
    animal_type = request.args.get('Animal_Type')
    sex_upon_intake = request.args.get('sexuponintake')
    age_upon_intake = request.args.get('ageuponintake')

    animal_intake = {}
    for i in dataframe['intakes data']:
        if i['Animal_ID'] == animal_id:
            i['Intake Type'] = intake_type
            i['Intake Condition'] = intake_condition
            i['Animal_Type'] = animal_type
            i['sexuponintake'] = sex_upon_intake
            i['ageuponintake'] = age_upon_intake

    rd_data.set('key', json.dumps(dataframe))
    return json.dumps(intake, indent = 4)

@app.route('/Terminate/', methods=['GET'])
def delete():
    dataframe = get_data()
    animal_id = request.args.get('Animal_ID')
    for i in dataframe['intakes']:

        if i['Animal ID'] == animal_id:
            dataframe['intakes'].remove(i)

    rd_jobs.set('intakes_key', json.dumps(dataframe))

    return 'ID {} is deleted.'.format(animal_id)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

@app.route('/jobs', methods=['POST']) #Jobrequest is issued and route will use graph in worker file                                                                                                                                     
def jobs_api():
    try:
        job = request.get_json(force=True)
    except Exception as e:
        return True, json.dumps({'status': "Error", 'message': 'Invalid JSON: {}.'.format(e)})
    return json.dumps(jobs.add_job(job['start'], job['end']))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
