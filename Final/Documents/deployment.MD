BUILD AN IMAGE

1.) docker build -t adkar47/adkar47-final .

2.) docker push adkar47/adkar47-final

DEPLOY ON K8

1.)kubectl apply -f adkar47-final-flask-deployment.yml 

2.)kubectl apply -f adkar47-final-flask-service.yml 

3.)kubectl apply -f adkar47-final-redis-deployment.yml

4.)kubectl apply -f adkar47-final-redis-service.yml

5.)kubectl apply -f adkar47-final-redis-pvc.yml

6.)kubectl apply -f adkar47-final-worker-deployment.yml

"Will give a created deployment/apps or service created line"

7.) kubectl get pods (Make Sure they are all running and if not redo the docker build, docker push, kubectl get pods Steps)

NAME                                               READY   STATUS    RESTARTS   AGE

adkar47-final-flask-deployment-57669f4c7b-tzh76    1/1     Running   0          43m

adkar47-final-redis-deployment-5b5869c567-66n8n    1/1     Running   0          168m

adkar47-final-worker-deployment-66469d94d4-5wt4r   1/1     Running   0          16s

8.) Note the Service IP address for the curl you will do: kubectl get services

NAME                          TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE

adkar47-final-flask-service   ClusterIP   10.99.255.213   <none>        5000/TCP         3h26m
  
adkar47-final-redis-service   ClusterIP   10.108.43.109   <none>        6379/TCP         3h25m
  
9.)Check stautus of pvc: kubectl get pvc

NAME                      STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
adkar47-final-redis-pvc   Bound    pvc-bcb0f238-7408-4b9e-a039-b4e29245e02a   1Gi        RWO            rbd            3h25m
