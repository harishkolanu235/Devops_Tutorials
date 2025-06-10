1. What is a Pod in Kubernetes? Create a pod.yaml for a single-container pod running Nginx.

    - A Pod is small deployment and its reprasent a group of one or more containers that shares resources like storage volumes and network, and a specification for how to run the containers.
    
    - Pods are ephemeral by nature, its not self-healing. if pod dies, it will not create automatically but kubernetes can create a new pod via a controller like a Deployment or RepliacaSet.

    ~~~
    apiVersion: v1
    kind: Pod
    metadata:
      name: nginx-pod
    spec:
      containers:
      - name: nginx-container
        image: nginx:latest
        ports:
        - containerPort: 80
    ~~~
2. What is init container?
3. What is sidecar container?
4. What is ephemeral container?
5. What is a Deployment in Kubernetes? Write a deployment.yaml for deploying 3 replicas of an Nginx container.

    - Deployment is a higher-level resource used to manage Pods and ReplicaSets. It provides a declarative way to deploy, update, and scale your applications.
    
    - It defines the desired state of your application, specifying things like the number of replicas (instances) of your application.

    - It supports self-healing, scaling, rollout and rollback.

        **self-healing:** If a Pod goes down, the Deployment ensures it's recreated to maintain the desired state.

        **scalling:**  You can easily scale the number of replicas up or down with a single command or by changing the YAML.

        **roll-out:** Automatically rolls out updates to Pods without downtime.

        **roll-out:** we can rolling back to a previous version if something goes wrong.
    ~~~
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: nginx-deployment
        labels:
          app: nginx
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: nginx
      template:
        metadata:
          labels:
            app: nginx
        spec:
          containers:
          - name: nginx-container
            image: nginx:latest
            ports:
              - containerPort: 80
    ~~~
6. What is demonset?
7. What is statefullset?

8. What is a Service in Kubernetes, and what are the types of Services?
9. When would you use each type of Kubernetes Service (ClusterIP, NodePort, LoadBalancer, ExternalName)?


10. Explain port, targetPort, and nodePort in a Kubernetes service.
11. How would you expose a Kubernetes application externally?
12. What is Helm, and what are its components (Chart, Repository, Release)?
13. What is the difference between EXPOSE in a Dockerfile and docker run -p?
14. How do you run Nginx on a Linux server using Docker?
15. Explain HTTP, HTTPS, TCP, and UDP with examples.
16. What is a Dockerfile? Write a basic Dockerfile for a Node.js application.
17. What is a base image in Docker? Which base image would you use for Python or Node.js?
18. How do you check for open ports on a Linux system?
19. What are the benefits of using a firewall?
20. What is the use of Ingress and Ingress Controller in Kubernetes?
21. Explain the Kubernetes controllers: Deployment, StatefulSet, ReplicaSet, and DaemonSet.
22. What is the difference between Deployment and ReplicaSet?
23. What are Kubernetes Probes (Liveness, Readiness, Startup)?
24. What is the difference between Stateful and Stateless applications? Give examples.
25. What are Namespaces in Kubernetes?
26. What is Port Forwarding in Kubernetes?

27. A Pod is stuck in CrashLoopBackOff. How do you troubleshoot it?
    ~~~
    ✅ Check logs: kubectl logs <pod-name>

    ✅ Describe pod: kubectl describe pod <pod-name>

    ✅ Check events & limits: Look for OOMKilled, failing readiness probes, or image issues.
    ~~~
    
28. Your application is running slow inside a Pod. How do you debug it?
    ~~~
    ✅ Check resource usage: kubectl top pod <pod-name>

    ✅ Check node performance: kubectl top nodes

    ✅ View pod logs & events: kubectl logs and kubectl describe pod

    ✅ Run debugging commands: kubectl exec -it <pod-name> -- sh
    ~~~

29. A Service is not reachable inside the cluster. How do you diagnose it?

    ~~~
    ✅ Check if the Service exists: kubectl get svc

    ✅ Verify the endpoints: kubectl get endpoints <service-name>

    ✅ Ensure correct port mapping: kubectl describe svc <service-name>

    ✅ Debug with busybox: kubectl run -it --rm busybox -- /bin/sh and nc -zv <service-ip> <port>
    ~~~

30. You need to roll back a failed Deployment. What do you do?

    ~~~
    ✅ Check the history: kubectl rollout history deployment <deployment-name>

    ✅ Roll back to a previous version: kubectl rollout undo deployment <deployment-name>

    ✅ Monitor rollout status: kubectl rollout status deployment <deployment-name>
    ~~~

31. A Node is NotReady. How do you investigate?

    ~~~
    ✅ Describe the node: kubectl describe node <node-name>

    ✅ Check Kubelet logs: journalctl -u kubelet -f

    ✅ Verify network & disk issues: kubectl get events --field-selector involvedObject.kind=Node
    ~~~

32. A Pod should run only on specific nodes. How do you enforce this?

    ~~~
    ✅ Use nodeSelector in the Pod spec.

    ✅ Define nodeAffinity for advanced scheduling.

    ✅ Use taints & tolerations to restrict pod placement.
    ~~~

33. You need to auto-scale your Pods based on CPU usage. How do you do it?

    ~~~
    ✅ Enable Horizontal Pod Autoscaler (HPA):kubectl autoscale deployment <deployment-name> --cpu-percent=50 --min=2 --max=10

    ✅ Ensure Metrics Server is installed: kubectl top pods
    ~~~

34. Your Pods are getting evicted. What could be the reason?

    ~~~
    ✅ Check node pressure: kubectl describe node <node-name>

    ✅ Verify resource limits: Insufficient memory or disk space can trigger evictions.

    ✅ Check taints: Nodes with NoSchedule taints may cause pod evictions.
    ~~~

35. A Secret is mounted inside a Pod but not working. How do you fix it?
    
    ~~~
    ✅ Check if the Secret exists: kubectl get secrets

    ✅ Verify the Pod’s volume mounts: kubectl describe pod <pod-name>

    ✅ Ensure the correct key is referenced: envFrom vs env in Deployment YAML.
    ~~~

36. You need to migrate an application from one cluster to another. What's the best approach?
    
    ~~~
    ✅ Backup & restore resources using kubectl get all -o yaml > backup.yaml

    ✅ Migrate Persistent Volumes using snapshots (AWS EBS, Azure Disks, etc.)
    
    ✅ Use GitOps tools like ArgoCD or FluxCD for deployment consistency.
    ~~~

