PROJECT DATA: Animal Center Intakes from Oct, 1st 2013 to present. Intakes represent animals brought to the center by citizens or Animal Services staff. Animals may be brought to the center as lost, injured or for the purpose of adoption. Animals may also be brought to the center as Public Assist. The found location is often only an estimation of where the animal was found. All animals receive a unique Animal ID during intake.

Over 120,000 rows of data from 2013 until new updates today. The table columns consist of animal_id, name, datetime, monthyear, found_location, intake_type, intake_condtion, animal_type, sex_upon_intake, age_upon_intake and breed 

Raw data in CSV and json from is available in the data directory

1.) Exec into python debug file using: kubectl exec -it py-debug-deployment-5cc8cdd65f-gg774  -- /bin/bash

2.) Copy your flask URL before any curl route like: root@py-debug-deployment-5cc8cdd65f-gg774:/# curl 10.99.255.213:5000/

3.) Route Functionality:

/populate : Will populate the Data into the database (1)

/Insert : C in CRUD, Can add a new intake species from the json list (2)

/Obtain_Intake : R in CRUD, Can query an animal based on the aninal id tag given in the described dataset (3)

/Update/ : U in CRUD, can update an animals feautres from the json list (4)

/terminate : D in CRUD, deletes a job or animal by the animal ID number given (5)

/jobs : job request will be graphed by datetime in the worker file (6)

1.) curl 10.99.255.213:5000/populate -X POST

{'animal_id': 'A820013', 'name': 'Dubi', 'datetime': '2021-05-07T08:48:00.000', 'datetime2': '2021-05-07T08:48:00.000', 'found_location': '780 Bastrop Highway in Austin (TX)', 'intake_type': 'Public Assist', 'intake_condition': 'Normal', 'animal_type': 'Dog', 'sex_upon_intake': 'Neutered Male', 'age_upon_intake': '1 year', 'breed': 'Labrador Retriever/Pit Bull', 'color': 'Black'}

2.) curl -X POST -H "content-type: application/json" -d '{ "Animal ID":"A456321", "Name":"", "DateTime":"7/5/2014 9:08", "MonthYear":"5/5/2021 17:08", "Found Location":"value", "Intake Type":"value","Intake Condition":"value", "Animal Type":"value", "Sex upon Intake":"value", "Age upon Intake":"value", "Breed":"value","Color":"value" }}'   10.99.255.213:5000/Insert

(Place a date value that matches the key structure in "Value" slots to create a new animal)

3.)curl 10.99.255.213:5000/Obtain_Intake/?Animal_ID=A760053 (Will query for an animal)

Output: {'animal_id': 'A820012', 'name': 'Sadie Mae', 'datetime': '2021-05-07T08:48:00.000', 'datetime2': '2021-05-07T08:48:00.000', 'found_location': '780 Bastrop Highway in Austin (TX)', 'intake_type': 'Public Assist', 'intake_condition': 'Normal', 'animal_type': 'Dog', 'sex_upon_intake': 'Spayed Female', 'age_upon_intake': '1 year', 'breed': 'Labrador Retriever', 'color': 'Black/White'}

4.) curl 10.99.255.213:5000/Update/?Animal_ID=A806287&name=Jack&intaketype=Stray&intakecondition=(Value)&animaltype=(value)&breed=(Tabby)&Color=(value)

Result: 5]- Done          animaltype=Cat
[6]+ Done                 breed=Tabby

5.) curl 10.99.255.213:5000/Terminate/?Animal_ID=A783861

(Will delete based on get_data initialized in jobs.py)

6.)curl -X POST -d  10.99.255.213:5000

Will submit a new job request
