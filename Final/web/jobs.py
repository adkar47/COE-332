import pandas as pd
from datetime import datetime
import uuid
from hotqueue import HotQueue
from redis import StrictRedis
import os

q = HotQueue("queue", host='10.108.43.109', port=6379, db=1)
rd_jobs = StrictRedis(host='10.108.43.109', port=6379, db=0)
rd_data = StrictRedis(host='10.108.43.109', port=6379, db=2)

                                                                                                                                     
#pizza_chain1 = pd.read_csv('https://query.data.world/s/fhrkutpspa5tbo2intmhzgzayppy3z').fillna(0) #First location on datainfiniti for pizza stores                                      
#pizza_chain2 = pd.read_csv('https://query.data.world/s/4ln24fqsirpq4krho4clki6wvaqbwy').fillna(0) #Second location on datainfiniti for pizza stores                                     

#master_chain = pd.merge(pizza_chain1, pizza_chain2, how='left', left_on= ['id', 'address', 'categories'], right_on = ['id', 'address','categories']).fillna(0) #Combining the data for \
                                                                                                                                  
#master_chain = master_chain.sort_values(by=['id','address','categories']) #Only using the first three columns of the dataset: the id, address, and category                             

def get_data(): #returns a dictionary                                                                                                                                                    
   data = {}
   for key in rd_data.keys():
       data['key'] = rd_data.hgetall('key')
   return data

def _generate_jid():
    return str(uuid.uuid4())

def _generate_job_key(jid):
    if type(jid) == bytes:
        jid = jid.decode('utf-8')
    return 'job.{}'.format(jid)

def _instantiate_job(jid, status, start, end):
    if type(jid) == str:
        return {'id': jid,
                'status': status,
                'start': start,
                'end': end
        }
    return {'id': jid.decode('utf-8'),
            'status': status.decode('utf-8'),
            'start': start.decode('utf-8'),
            'end': end.decode('utf-8')
    }

def _save_job(job_key, job_dict):
    """Save a job object in the Redis database."""
    rd_jobs.hmset(job_key, job_dict)

def _queue_job(jid):
    """Add a job to the redis queue."""
    q.put(jid)

def add_job(start, end, status="submitted"):
    """Add a job to the redis queue."""
    jid = _generate_jid()
    job_dict = _instantiate_job(jid, status, start, end)    # updates the save job:                                                                                                      
    _save_job(_generate_job_key(jid), job_dict) # updates the queue job:                                                                                                                 
    _queue_job(jid)
    return job_dict


def update_job_status(jid, new_status):
    """Update the status of job with job id `jid` to status `status`."""
    jid, status, start, end = rd.hmget(_generate_job_key(jid), 'id', 'status', 'start', 'end', 'animal_type', 'sex_upon_intake')
    job = _instantiate_job(jid, status, start, end)

    if(new_status == 'in progress'):
        worker_IP = os.environ.get('WORKER_IP')
        print(worker_IP)
        rd_jobs.hset(_generate_job_key(jid), 'worker', worker_IP)

    if job:
        job['status'] = new_status
        _save_job(_generate_job_key(job['id']), job)
    else:
        raise Exception()
