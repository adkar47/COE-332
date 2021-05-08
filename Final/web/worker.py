from jobs import q, update_job_status
import redis
import time
import pandas as pd
import matplotlib.pyplot as plt
import datetime

rd_job = redis.StrictRedis(host= '10.108.43.109' , port=6379, db=0)
rd_data = redis.StrictRedis(host= '10.108.43.109', port=6379, db=0)

                                                                                                                                   \


@q.worker
def execute_job(jid): #Part B in creating a graph of the Animal Type from dataworlds data set of Austin Animal Center               

    # Use rd_job for the generate job key function from the dataset                                                                 
    jobid, status, start, end = rd_job.hmget(generate_job_key(jid), 'id', 'status', 'start', 'end', 'animal_type')
    dataset = json.loads(rd.get('data'))
    x_data = [] #Time as the independent variable which intakes from citizens depends on                                            
    y_data = [] #Intakes of animals brough by citizens or animal services                                                           


    start = job['begin']
    end = job['end']


    beginningDate = datetime.datetime.strptime(start,'%m-$d-%Y') #datetime structure used in midterm                                
    endingDate = datetime.datetime.strptime(end, '%m-%d-$Y')


    base_count = 0
    for key in rd_data.keys():
        datetime = str(rd_data.get(key, 'DateTime'))
        if (start<=datetime):
            x_data.append(key)
            y_data.append(key)

#Structure                                                                                                                          
#x = np.linspace(0, 2*np.pi, 50)                                                                                                    
#plt.plot(x, np.sin(x))                                                                                                             
#plt.show() # we can't do this on our VM server                                                                                     
#plt.savefig('my_sinwave.png')                                                                                                      

    plt.scatter(x_data, y_data) #Refer back to lecture on matplotlib                                                                
    plt.xlabel('Time')

    plt.ylabel('Amount of Intake Types')

    plt.title('Time vs number of intakes')

    plt.show()

    plt.savefig('/output_Animal_Center.png')


    with open('/my_Animal_Center.png') as f:
        image = f.read()

    rd_data.hset(jid, 'image', image)
    rd_data.hset(jid, 'status', 'completed ')

if __name__ == '__main__':

    execute_job()
