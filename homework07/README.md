HOMEWORK 07


1.) First use the command kubectl -f apply () to all of the YAML files 

2.) Ensure that all of pods are running by using the command: kubectl get pods

3.) Use command kubectl get services to find your flask and redis Cluster IP address to add to your jobs.py file

4.) Run kubectl exec -it py-debug-deployment-5cc8cdd65f-gg774  -- /bin/bash AFTER you have built your Docker file and pushed to Docker hub

5.)Inside the pod run: curl -X POST -H "content-type: application/json" -d '{"start": "start", "end": "end"}' 10.111.58.243:5000/jobs

Result: {"id": "2f3c55d3-103c-4217-9284-738bb102b5b5", "status": "submitted", "start": "start", "end": "end"}root@py-debug-deployment-5cc8cdd65f-gg774:/# python

6.) Ensure it is functioning by running a python interface within the pod:

import redis
rd = redis.StrictRedis(host='10.111.54.132', port = 6379, db =0)
rd.keys()

7.) New worker tag updated within the jobs.py script

def update_job_status(jid, new_status):


    """Update the status of job with job id `jid` to status `status`."""
    
    
    jid, status, start, end = rd.hmget(_generate_job_key(jid), 'id', 'status', 'start', 'end')
    
    
    job = _instantiate_job(jid, status, start, end)
    
    
    if job:
    
    
        job['status'] = new_status
        
        
        job['worker'] = os.environ['WORKER_IP']
        
        
        _save_job(_generate_job_key(job['id']), job)
        
        
    else:
    
   
        raise Exception()
