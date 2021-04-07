 A

1.) Run kubectl -f apply A_pod.yml
2.) Run the command kubectl get pods then get the pod's logs by typing kubectl logs pod/hello

[adkar47@isp02 homework05]$ kubectl apply -f A_pod.yml you should see the pod hello created command which was expected
pod/hello created

3.) Delete the pod using kubectl delete pods hello

[adkar47@isp02 homework05]$ kubectl delete pods hello  
pod "hello" deleted

 B

1.) Use the same kubectl apply command for B_pod.yml
2.) Run kubectl logs pod/hello Hello ("Name") should appear

[adkar47@isp02 homework05]$ kubectl logs pod/hello

Hello, Adhi!

4.) Delete the pod using kubectl delete pods hello


C

1.) Use the same step 1 from previous two parts 
2.) Run kubectl get pods -o wide , which will output the deplyoment status and the IP address 
3.) Check if the IP address matches from the ones created in part 2

NAME                                READY   STATUS    RESTARTS   AGE    IP             NODE                         NOMINATED NODE   READINESS GATES
hello-deployment-55f4459bf-84p2c    1/1     Running   0          5m     10.244.6.154   c03                          <none>           <none>
helloflask-848c4fb54f-gqhfd         1/1     Running   0          4m6s   10.244.10.6    c009.rodeo.tacc.utexas.edu   <none>           <none>
partc-deployment-578c9cfcf6-27f7d   1/1     Running   18         18h    10.244.3.78    c01                          <none>           <none>
partc-deployment-578c9cfcf6-6lvv5   1/1     Running   18         18h    10.244.4.129   c02                          <none>           <none>
partc-deployment-578c9cfcf6-k7lqk   1/1     Running   18         18h    10.244.10.2    c009.rodeo.tacc.utexas.edu   <none>           <none>

4.) In order to get the pods logs run kubectl logs --selector "greeting"
Hello, Adhi from IP 10.244.3.78
Hello, Adhi from IP 10.244.4.129
Hello, Adhi from IP 10.244.10.2
