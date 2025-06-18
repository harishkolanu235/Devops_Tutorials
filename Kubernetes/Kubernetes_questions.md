#### 1. What is a Pod in Kubernetes? Create a pod.yaml for a single-container pod running Nginx.

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

#### 2. What is init container?

  - init container is type of container that run before main application container in a Pod. Init containers can contain utilities or setup scripts not present in an app image.
  - They are primarily used to perform initialization tasks that must complete successfully before the main containers start.
  - If an init container fails, Kubernetes retries until it succeeds or the Pod fails.
  - Init containers run in the same Pod (thus same network & volumes) but are separate from app containers.
  - Below are the use cased
    - Setting up config files
    - Waiting for services (like databases) to be ready
    - Downloading dependencies
    - Running setup scripts

    ~~~
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: myapp
      labels:
        app: myapp
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: myapp
      template:
        metadata:
          labels:
            app: myapp
        spec:
          initContainers:
            - name: logshipper
              image: alpine:latest
              restartPolicy: Always
              command: ['sh', '-c', 'tail -F /opt/logs.txt']
              volumeMounts:
                - name: data
                  mountPath: /opt
          containers:
            - name: myapp
              image: alpine:latest
              command: ['sh', '-c', 'while true; do echo "logging" >> /opt/logs.txt; sleep 1; done']
              volumeMounts:
                - name: data
                  mountPath: /opt
          
          volumes:
            - name: data
              emptyDir: {}
    ~~~

#### 3. What is sidecar container?
  
  - Sidecar containers are the secondary containers that run along with the main application container within the same Pod.
  - These containers are used to enhance or to extend the functionality of the primary app container by providing additional services, or functionality such as logging, monitoring, security, or data synchronization, without directly altering the primary application code.
  -  For example, if you have a web application that requires a local webserver, the local webserver is a sidecar and the web application itself is the app container

#### 4. What is ephemeral container?

  - Its a special type of container that runs temporarily in an existing Pod to accomplish user-initiated actions such as troubleshooting.

#### 5. What is a Deployment in Kubernetes? Write a deployment.yaml for deploying 3 replicas of an Nginx container.

    - Deployment is a higher-level resource used to manage Pods and ReplicaSets. It provides a declarative way to deploy, update, and scale your applications.
    
    - It defines the desired state of your application, specifying things like the number of replicas (instances) of your application.

    - It supports self-healing, scaling, rollout and rollback.

        **self-healing:** If a Pod goes down, the Deployment ensures it's recreated to maintain the desired state.

        **scalling:**  You can easily scale the number of replicas up or down with a single command or by changing the YAML.

        **roll-out:** Automatically rolls out updates to Pods without downtime.

        **roll-back:** we can rolling back to a previous version if something goes wrong.
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
#### 6. What is demonset? Why use DaemonSet?

  - DaemonSet ensures that a pod is running on every node in the cluster that matches a given selector, or on a subset of nodes. 
  - It's designed for node-specific tasks like logging, monitoring, or storage provisioning. 

  **Use-cases**

  - To ensure logs are captured from all nodes.
  - To run metrics exporters like Node Exporter.
  - To install CNI plugins or storage drivers on every node

#### 7. What is statefullset? why use statefullset?

  - StatefulSet manages stateful applications that require persistent storage, stable network identifiers, and ordered deployment and scaling.
  - Unlike Deployments, which are used for stateless applications, StatefulSets provide a way to maintain persistent identities and ordered scaling for Pods.
  - Each Pod gets a stable hostname (e.g., pod-0, pod-1, etc.) that never changes across rescheduling.
  - Each Pod can have its own PersistentVolumeClaim (PVC), ensuring data persists across restarts.
  - Pods are created, updated, and deleted in order (pod-0 first, then pod-1, etc.).
  - use-cases: Databases (MySQL, MongoDB, Cassandra), Zookeeper, Kafka — any app where state matters.

    **why use it**
  - Need persistent storage and stable Pod names for cluster membership.
  - Require stable network identity and start/stop ordering.

#### 8. What is a Service in Kubernetes, and what are the types of Services?

  - By using service, it can be enable the network access to them.

  **Why Service is needed**

    - Pods are ephemeral — they can die, restart, or be replaced anytime.
    - Each Pod has its own IP address but this IP is not permanent.
    - To allow stable communication to these changing Pods, a Service is used.

  **Types of Services**

    - ClusterIP (default) ----> Exposes the Service on an internal IP in the cluster. Accessible only within the cluster.

    - Node Port ----> Exposes the Service on each Node's IP at a static port. External traffic can access the Service via <NodeIP>:<NodePort>.

    - LoadBalancer ----> Maps the Service to a DNS name (outside the cluster) instead of a Pod. It will get public ip to access the app.

  ~~~
    apiVersion: v1
    kind: Service
    metadata:
      name: my-service
    spec:
      selector:
        app: my-app    # Targets Pods with this label
      ports:
        - protocol: TCP
          port: 80         # Port exposed by the Service
          targetPort: 8080 # Port on the Pod
      type: ClusterIP

  ~~~

#### 9. How would you expose a Kubernetes application externally?
  - to expose an application externally (outside the cluster), you can use any of the following methods:
    - **NodePort Service**
    ~~~
      apiVersion: v1
      kind: Service
      metadata:
        name: my-app-service
      spec:
        type: NodePort
        selector:
          app: my-app
        ports:
          - port: 80
            targetPort: 8080
            nodePort: 30080  # Exposed port on the node
    ~~~

    - **LoadBalancer Service**
      - Automatically provisions an external Load Balancer.
      - You get a public IP to access the app.
    ~~~
      apiVersion: v1
      kind: Service
      metadata:
        name: my-app-service
      spec:
        type: LoadBalancer
        selector:
          app: my-app
        ports:
          - port: 80
            targetPort: 8080

    ~~~

    - **Ingress Resource** ----> Provides HTTP routing via path or host-based rules.
    ~~~
      apiVersion: networking.k8s.io/v1
      kind: Ingress
      metadata:
        name: my-app-ingress
      spec:
        rules:
        - host: myapp.example.com
          http:
            paths:
            - path: /
              pathType: Prefix
              backend:
                service:
                  name: my-app-service
                  port:
                    number: 80

    ~~~
#### 10. What is Helm, and what are its components (Chart, Repository, Release)?

  - Helm is a package manager for Kubernetes, similar to APT (Debian) or YUM (RHEL).
It simplifies deploying, configuring, and managing applications in Kubernetes by packaging resources into "Charts".

**Helm Components**
  - **Charts** 
    - Contains all the Kubernetes resource definitions (YAML files) needed to run an app, such as Deployments, Services, ConfigMaps, etc.
    - A Chart can be parameterized using variables (values.yaml).

  - **Repository** ---> A place where Charts are stored and shared.Similar to Docker Registry or Git repo.
    ~~~
    $ helm repo add bitnami https://charts.bitnami.com/bitnami
    
    $ helm repo update
    
    $ helm search repo nginx
    ~~~
  - **Release**
    - You can install multiple Releases from the same Chart with different names/configurations.
    ~~~
    $ helm install my-nginx bitnami/nginx   # Creates a Release called 'my-nginx'
    ~~~

#### 11. What is the difference between EXPOSE in a Dockerfile and docker run -p?

  - EXPOSE 80 just declares that the container listens on port 80, but does not publish it to the host.

  - -p 8080:80 actually makes port 80 inside the container accessible as port 8080 on the host.


#### 12. What is the use of Ingress and Ingress Controller in Kubernetes?

  - Ingress is an API object in Kubernetes that manages external access to services within the cluster
  - It allows you to define rules to route traffic to different services based on:
    - Hostnames (e.g., app.example.com)
    - Paths (e.g., /api, /login)
  ~~~
  apiVersion: networking.k8s.io/v1
  kind: Ingress
  metadata:
    name: example-ingress
  spec:
    rules:
    - host: myapp.example.com
      http:
        paths:
        - path: /
          pathType: Prefix
          backend:
            service:
              name: my-service
              port:
                number: 80
  ~~~

  **The Ingress Controller** is the actual component (pod) that:

    - Watches Ingress resources.
    - Processes Ingress rules.
    - Configures a reverse proxy (like NGINX, Traefik, HAProxy) to direct traffic accordingly.
    - Without an Ingress Controller, an Ingress resource does nothing — it’s just a config file.


#### 13. What is the difference between Deployment and ReplicaSet?
  **ReplicaSet**

    - A ReplicaSet (RS) ensures that a specified number of pod replicas are running at any given time.
    - It can scale up or down pods to match the desired replica count.
    - On its own, ReplicaSet lacks advanced features like rollout, rollback, or versioning.
  **Deployment**
  - A Deployment manages a ReplicaSet and adds features such as:
    - Rolling updates
    - Rollbacks
    - Pause/Resume deployments
    - History tracking
  - Deployment automatically creates and manages ReplicaSets in the background.

#### 14. What are Kubernetes Probe?

  **Liveness**
    - Checks if the container is alive (running properly).
    - If its fails, Kubernetes will kill and restart the container.

      ~~~
      livenessProbe:
      httpGet:
        path: /healthz
        port: 8080
      initialDelaySeconds: 5
      periodSeconds: 10
      ~~~

  **Readiness**

    - Checks if the container is ready to serve traffic.
    - If it fails, Kubernetes removes the pod from Service endpoints, but doesn’t restart it.

    ~~~
    readinessProbe:
    httpGet:
      path: /ready
      port: 8080
    initialDelaySeconds: 5
    periodSeconds: 10
    ~~~

  **Startup**

    - Checks if the app within the container has started successfully.
    -  If it fails, Kubernetes restarts the container.

    ~~~
    startupProbe:
    httpGet:
      path: /startup
      port: 8080
    failureThreshold: 30
    periodSeconds: 10
    ~~~


#### 15. What is Port Forwarding in Kubernetes?
  - Port Forwarding in Kubernetes allows you to access a pod’s port directly from your local machine, without exposing it via a service or ingress to the outside world.
  - It's useful for debugging, development, or testing when you want to interact with a pod without deploying a full service or exposing it publicly.
  ~~~
  $ kubectl port-forward <pod-name> <local-port>:<pod-port>

  ~~~

#### 16. A Pod is stuck in CrashLoopBackOff. How do you troubleshoot it?
    ~~~
    ✅ Check logs: kubectl logs <pod-name>

    ✅ Describe pod: kubectl describe pod <pod-name>

    ✅ Check events & limits: Look for OOMKilled, failing readiness probes, or image issues.
    ~~~
    
#### 17. Your application is running slow inside a Pod. How do you debug it?
    ~~~
    ✅ Check resource usage: kubectl top pod <pod-name>

    ✅ Check node performance: kubectl top nodes

    ✅ View pod logs & events: kubectl logs and kubectl describe pod

    ✅ Run debugging commands: kubectl exec -it <pod-name> -- sh
    ~~~

#### 18. A Service is not reachable inside the cluster. How do you diagnose it?

    ~~~
    ✅ Check if the Service exists: kubectl get svc

    ✅ Verify the endpoints: kubectl get endpoints <service-name>

    ✅ Ensure correct port mapping: kubectl describe svc <service-name>

    ✅ Debug with busybox: kubectl run -it --rm busybox -- /bin/sh and nc -zv <service-ip> <port>
    ~~~

#### 19. You need to roll back a failed Deployment. What do you do?

    ~~~
    ✅ Check the history: kubectl rollout history deployment <deployment-name>

    ✅ Roll back to a previous version: kubectl rollout undo deployment <deployment-name>

    ✅ Monitor rollout status: kubectl rollout status deployment <deployment-name>
    ~~~

#### 20. A Node is NotReady. How do you investigate?

    ~~~
    ✅ Describe the node: kubectl describe node <node-name>

    ✅ Check Kubelet logs: journalctl -u kubelet -f

    ✅ Verify network & disk issues: kubectl get events --field-selector involvedObject.kind=Node
    ~~~

#### 21. A Pod should run only on specific nodes. How do you enforce this?

    ~~~
    ✅ Use nodeSelector in the Pod spec.

    ✅ Define nodeAffinity for advanced scheduling.

    ✅ Use taints & tolerations to restrict pod placement.
    ~~~

#### 22. You need to auto-scale your Pods based on CPU usage. How do you do it?

    ~~~
    ✅ Enable Horizontal Pod Autoscaler (HPA):kubectl autoscale deployment <deployment-name> --cpu-percent=50 --min=2 --max=10

    ✅ Ensure Metrics Server is installed: kubectl top pods
    ~~~

#### 23. Your Pods are getting evicted. What could be the reason?

    ~~~
    ✅ Check node pressure: kubectl describe node <node-name>

    ✅ Verify resource limits: Insufficient memory or disk space can trigger evictions.

    ✅ Check taints: Nodes with NoSchedule taints may cause pod evictions.
    ~~~

#### 24. A Secret is mounted inside a Pod but not working. How do you fix it?
    
    ~~~
    ✅ Check if the Secret exists: kubectl get secrets

    ✅ Verify the Pod’s volume mounts: kubectl describe pod <pod-name>

    ✅ Ensure the correct key is referenced: envFrom vs env in Deployment YAML.
    ~~~

#### 25. You need to migrate an application from one cluster to another. What's the best approach?
    
    ~~~
    ✅ Backup & restore resources using kubectl get all -o yaml > backup.yaml

    ✅ Migrate Persistent Volumes using snapshots (AWS EBS, Azure Disks, etc.)
    
    ✅ Use GitOps tools like ArgoCD or FluxCD for deployment consistency.
    ~~~

#### 26. If POD is deleted, how pod will re-create in kuberntes?
    - Pod is deleted in a Deployment/ReplicaSet, ReplicaSet notices the missing Pod and asks the API Server to create a new Pod.
    
    - Kubernetes Scheduler picks a suitable Node for this new Pod.
    
    - Once scheduled:
        - The Pod spec is stored in the API Server.
        - The Kubelet on the target Node continuously watches the API Server for any Pods assigned to it.
        
    - When Kubelet notices this new Pod assigned to its Node, it:
        - Downloads the container image (if needed).
        - Sets up networking.
        - Launches the container(s).
        - Manages liveness/readiness probes.

