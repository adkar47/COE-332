SERVICES FOR FLASK APP AND REDIS DATABASE

1.) RUN: kubectl apply -f adkar47-test-flask-service.yml

2.) RUN: kubectl apply -f adkar47-test-redis-service.yml
4.) RUN two pods one for flask deployment and another for Redis deployment
5.) RUN: kubectl get pods
NAME                                             READY   STATUS    RESTARTS   AGE
adkar47-test-flask-deployment-797b7db9bb-84d52   1/1     Running   0          73m
adkar47-test-flask-deployment-797b7db9bb-jsxj2   1/1     Running   0          73m
hello-deployment-55f4459bf-84p2c                 1/1     Running   170        7d2h
helloflask-848c4fb54f-gqhfd                      1/1     Running   0          7d2h
partc-deployment-578c9cfcf6-27f7d                1/1     Running   189        7d20h
partc-deployment-578c9cfcf6-6lvv5                1/1     Running   188        7d20h
partc-deployment-578c9cfcf6-k7lqk                1/1     Running   188        7d20h

5.) RUN: kubectl get services
NAME                         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)          AGE
adkar47-test-flask-service   ClusterIP   10.98.238.74    <none>        5000/TCP         3h34m
adkar47-test-redis-service   ClusterIP   10.97.21.171    <none>        6379/TCP         3h33m
app1                         NodePort    10.109.114.68   <none>        5000:31228/TCP   7d3h
  
6.) Next run the command kubectl exec -it adkar47-test-flask-deployment-797b7db9bb-84d52 -- /bin/bash
This will bring you inside the container within the pods shell which will now say "root"
7.) pip3 commands in the root pod and run the app routes from app.py through curl
