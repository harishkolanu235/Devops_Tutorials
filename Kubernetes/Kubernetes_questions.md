1. What is a Pod in Kubernetes? Create a pod.yaml for a single-container pod running Nginx.
2. What is a Deployment in Kubernetes? Write a deployment.yaml for deploying 3 replicas of an Nginx container.
3. What is a Service in Kubernetes, and what are the types of Services?
4. When would you use each type of Kubernetes Service (ClusterIP, NodePort, LoadBalancer, ExternalName)?
5. Write a simple Terraform script to provision a virtual machine on AWS.
6. Explain port, targetPort, and nodePort in a Kubernetes service.
7. How would you expose a Kubernetes application externally?
8. What is Helm, and what are its components (Chart, Repository, Release)?
9. What is the difference between EXPOSE in a Dockerfile and docker run -p?
10. How do you run Nginx on a Linux server using Docker?
11. Explain HTTP, HTTPS, TCP, and UDP with examples.
12. What is a Dockerfile? Write a basic Dockerfile for a Node.js application.
13. What is a base image in Docker? Which base image would you use for Python or Node.js?
14. How do you check for open ports on a Linux system?
15. What are the benefits of using a firewall?
16. What is the use of Ingress and Ingress Controller in Kubernetes?
17. Explain the Kubernetes controllers: Deployment, StatefulSet, ReplicaSet, and DaemonSet.
18. What is the difference between Deployment and ReplicaSet?
19. What are Kubernetes Probes (Liveness, Readiness, Startup)?
20. What is the difference between Stateful and Stateless applications? Give examples.
21. What are Namespaces in Kubernetes?
22. What is Port Forwarding in Kubernetes?

23. A Pod is stuck in CrashLoopBackOff. How do you troubleshoot it?
    ~~~
    ✅ Check logs: kubectl logs <pod-name>

    ✅ Describe pod: kubectl describe pod <pod-name>

    ✅ Check events & limits: Look for OOMKilled, failing readiness probes, or image issues.
    ~~~
    
24. Your application is running slow inside a Pod. How do you debug it?
    ~~~
    ✅ Check resource usage: kubectl top pod <pod-name>

    ✅ Check node performance: kubectl top nodes

    ✅ View pod logs & events: kubectl logs and kubectl describe pod

    ✅ Run debugging commands: kubectl exec -it <pod-name> -- sh
    ~~~

25. A Service is not reachable inside the cluster. How do you diagnose it?

    ~~~
    ✅ Check if the Service exists: kubectl get svc

    ✅ Verify the endpoints: kubectl get endpoints <service-name>

    ✅ Ensure correct port mapping: kubectl describe svc <service-name>

    ✅ Debug with busybox: kubectl run -it --rm busybox -- /bin/sh and nc -zv <service-ip> <port>
    ~~~

26. You need to roll back a failed Deployment. What do you do?

    ~~~
    ✅ Check the history: kubectl rollout history deployment <deployment-name>

    ✅ Roll back to a previous version: kubectl rollout undo deployment <deployment-name>

    ✅ Monitor rollout status: kubectl rollout status deployment <deployment-name>
    ~~~

27. A Node is NotReady. How do you investigate?

    ~~~
    ✅ Describe the node: kubectl describe node <node-name>

    ✅ Check Kubelet logs: journalctl -u kubelet -f

    ✅ Verify network & disk issues: kubectl get events --field-selector involvedObject.kind=Node
    ~~~

28. A Pod should run only on specific nodes. How do you enforce this?

    ~~~
    ✅ Use nodeSelector in the Pod spec.

    ✅ Define nodeAffinity for advanced scheduling.

    ✅ Use taints & tolerations to restrict pod placement.
    ~~~

29. You need to auto-scale your Pods based on CPU usage. How do you do it?

    ~~~
    ✅ Enable Horizontal Pod Autoscaler (HPA):kubectl autoscale deployment <deployment-name> --cpu-percent=50 --min=2 --max=10

    ✅ Ensure Metrics Server is installed: kubectl top pods
    ~~~

30. Your Pods are getting evicted. What could be the reason?

    ~~~
    ✅ Check node pressure: kubectl describe node <node-name>

    ✅ Verify resource limits: Insufficient memory or disk space can trigger evictions.

    ✅ Check taints: Nodes with NoSchedule taints may cause pod evictions.
    ~~~

31. A Secret is mounted inside a Pod but not working. How do you fix it?
    
    ~~~
    ✅ Check if the Secret exists: kubectl get secrets

    ✅ Verify the Pod’s volume mounts: kubectl describe pod <pod-name>

    ✅ Ensure the correct key is referenced: envFrom vs env in Deployment YAML.
    ~~~

32. You need to migrate an application from one cluster to another. What's the best approach?
    
    ~~~
    ✅ Backup & restore resources using kubectl get all -o yaml > backup.yaml

    ✅ Migrate Persistent Volumes using snapshots (AWS EBS, Azure Disks, etc.)
    
    ✅ Use GitOps tools like ArgoCD or FluxCD for deployment consistency.
    ~~~

