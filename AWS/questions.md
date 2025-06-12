## Networking Questions

1. What is the use of Subnets?
    
    When a network has lot of HOSTS, managing these hosts can be tedious under a single large network. Therefore, we divide this large network into easily manageable sub-networks (subnets) so that managing hosts under each subnet becomes easier.

2. What is router?

    A router is a device that forwards data packets along networks. A router is connected to at least two networks, commonly two LANs or WANs or LAN and its ISP’s network. 

3. What is the use of Route Table?
    
    Route Table is used to route the network pockets. Generally, one route table would be available in each subnet. Route table can have any no. of records or information, hence attaching multiple subnets to a route table is also possible.

4. What is Security Group?
    
    - A security group acts as a virtual firewall that controls the inbound and outbound traffic for one or more instances. When you launch an instance, you can specify one or more security groups; otherwise, we use the default security group.
    - You can add rules to each security group that allow traffic to or from its associated instances. 
    - inbound traffic that's allowed to reach the instances that are associated with the security group and the outbound traffic that's allowed to leave them.

5. List the components required to build Amazon VPC?

    Subnet, Internet Gateway, NAT Gateway, Virtual Private Gateway, Customer Gateway, Router, Peering Connection, VPC Endpoint for S3, Egress-only Internet Gateway.

6. In a VPC how many EC2 instances can you use?

    Initially you are limited to launch 20 EC2 Instances at one time. Maximum VPC size is 65,536 instances.

7. Can you establish a peering connection to a VPC in a different REGION?

    Not possible. Peering Connection are available only between VPC in the same region.

8. Can you connect your VPC with a VPC owned by another AWS account?
    
    Yes, Possible. Provided the owner of other VPCs accepts your connection.

9. How do you connect my VPC to the Internet?
    
    Amazon VPC supports the creation of an Internet gateway. This gateway enables Amazon EC2 instances in the VPC to directly access the Internet.

10. How can you monitor network traffic in your VPC?
    
    It is possible using Amazon VPC Flow-Logs feature.

11. Difference between Security Groups and ACLs in a VPC?

    A Security Group defines which traffic is allowed TO or FROM EC2 instance. Whereas ACL, controls at the SUBNET level, scrutinize the traffic TO or FROM a Subnet.

12. What is public subnet?
    
    Public subnet is subnet in AWS. Which is associated with route table which has connected to the internet gateway.

13. What is private subnet?
    
    Private subnet is subnet in AWS. Which is associated with route table which hasn’t connected to the internet gateway.

14. What is NAT?
    
    NAT is a service to provide internet to a private subnet.  NAT should be deployed in Public subnet. And we will add private route to the NAT

15. What is bastion host?
    
    A machine which is in in the public subnet which helps to connect private subnet is called bastion host. 

## ELB Questions

16. What is Elastic Load balancing?
    
    - Elastic Load Balancing automatically distributes traffic across multiple targets – Amazon EC2 instances, containers and IP addresses – in a single Availability Zone or multiple Availability Zones. 
    - A load balancer distributes workloads across multiple compute resources, such as virtual servers. Using a load balancer increases the availability and fault tolerance of your applications.
    - You can add and remove compute resources from your load balancer as your needs change, without disrupting the overall flow of requests to your applications.
    - You can configure health checks, which are used to monitor the health of the compute resources so that the load balancer can send requests only to the healthy ones.

17. What are the types of Load Balancer?

    Elastic Load Balancing supports Three types of Load Balancers
    
    **Application Load Balancer**
    - An Application Load Balancer supports layer-7, layer-7 means application layer.
    - This load balancer makes routing decisions at the application layer (HTTP/HTTPS).
    - It supports path-based routing and host-based routing. 
    - You can route requests to one or more ports on each container instance in your cluster. 
    - Application Load Balancers support dynamic host port mapping.  

    **Network Load Balancer**

    - An Application Load Balancer supports layer-4, layer-4 means Transport layer.
    - A Network Load Balancer makes routing decisions at the transport layer (TCP/SSL).
    - It can handle millions of requests per second. After the load balancer receives a connection, it selects a target from the target group for the default rule using a flow hash routing algorithm.
    - In layer 4 the only understands the port number.  

    **Classic Load Balancer**

    - A Classic Load Balancer makes routing decisions at either the transport layer (TCP/SSL) or the application layer (HTTP/HTTPS). Classic Load Balancers currently require a fixed relationship between the load balancer port and the container instance port.



## Other Questions
18. Different types of Cloud Computing as per services?

    - PAAS (Platform As A Service), 
    - IAAS (Infrastructure As A Service), 
    - SAAS (Software As A Service)

19. What is Auto Scaling?
    
    Automatically Creating duplicate instances during heavy business hours. Scale-IN and Scale-OUT are two different statues of Scaling. Scale-IN: Reducing the instances. Scale-OUT: Increasing the instances by duplicating.

20. What is Horizontal and vertical scaling?

    - Vertical scaling refers to adding more resources (CPU/RAM/DISK) to your server (database or application server is still remaining one) as on demand.
    - Horizontal Scaling we can add one more server with same capacity along with existing server.

21. What is AMI?
    
    - AMI is a backup of Harddisk (snapshot), and metadata.it provides the information required to launch an instance, which is a virtual server in the cloud. You must specify a source AMI when you launch an instance. 
    - You can launch multiple instances from a single AMI when you need multiple instances with the same configuration. 
    - CLI provides AMI Id, that is different from one region to another.
    - You can use different AMIs to launch instances when you need instances with different configurations.

22. Difference between Stopping and Terminating the Instances?
    
    When you STOP an instance, it is a normal shutdown. The corresponding EBS volume attached to that instance remains attached and you can restart the instance later. When you TERMINATE an instance, it gets deleted and you cannot restart that instance again later. And any EBS volume attached with that instance also deleted.

23. What is S3?
    
    S3 stands for Simple Storage Service, with a simple web service interface to store and retrieve any amount of data from anywhere on the web. Its like a FTP storage. You can keep your SNAPSHOTS in S3. You can also ENCRYPT your sensitive data in S3.

24. Difference between S3 and EBS?

| S3 | EBS |
|----|-----|
| Can be publicly accessible | 	Accessible only via the given EC2 Machine |
| S3 is web interface |	EBS is filesystem interface |
| No limit on number of objects |	Maximum storage size of 16TB |
| Block storage with filesystems.|	Object storage |
| S3 can be used by multiple instances.|	EBS can only be used by one EC2 instance at a time.|
| EBS appears as a mountable volume. |	the S3 requires software to read and write data.|
| Its store large amount of data. |	EBS can accommodate a smaller amount of data than S3 |
| S3 is a static storage service useful for static website hosting, media distribution, version management, big data analytics, and archiving. | EBS is a persistent storage device that can be used as file system for databases, application hosting and storage and plug and play devices.|
| S3 is much cheaper than EBS	| |
|	| EBS is both faster than S3.|
|Access is based on IAM.	| |


25. What is AWS Lambada?
    
    Lambda is an event-driven platform. It is a compute service that runs code in response to events and automatically manages the compute resources required by that code.

26. In S3 how many buckets can be created?
    
    By default, 100 buckets can be created in a region.

27. Key Pair and its uses?
    
    You use Key Pair to login to your Instance in a secured way. You can create a key pair using EC2 console. When your instances are spread across regions you need to create key pair in each region.

28. Can you change the Private IP of an EC2 instance    while it is running or stopped?
    
    A Private IP is STATIC. And it is attached with an instance throughout is lifetime and cannot be changed.
