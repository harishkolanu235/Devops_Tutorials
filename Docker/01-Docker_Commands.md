# Docker Commands
---

1. To Display the Docker Version.
   ~~~
    # docker  -v	
    or	
    # docker  --version
    or
    # docker version
   ~~~

2. To Search  the images in public docker engine (Docker Hub).		
   ~~~
    # docker search immages
   ~~~

3. To search the particular image in public docker engine.	 
   ~~~
    # docker search <img_name>
    Ex: # docker search centos
   ~~~

4. To download the images to local docker engine.
   ~~~			
    # docker pull <img_name>
	Ex: # docker pull centos
   ~~~

5. To display the local docker engine images.	
   ~~~
    # docker images
   ~~~

6. To run the image as container
   ~~~
   # docker  run  -it  --name <container_name>   <img_name>   
   Ex:  # docker  run  -it  --name  centos_cnt1  centos   
   ~~~ 

7. To run the images as container with detach mode
    ~~~
    # docker  run  -d  --name <container_name>   <img_name>   
    Ex:  # docker  run  -d  --name  ubuntu_cnt2  ubuntu  
    ~~~

8. Entering into the container
    ~~~
    # docker  attach  <cid> or <name>
    Ex: # docker attach ubuntu_cnt2
    ~~~
    *Note:* To exit from the container without stoping the container.
    press ctr + p + q

9. To run the image as container with specific port
    ~~~
    # docker  run  -it  --name  <container_name>   -p  81:80  <img_name>
    ~~~
    *Note:* -p <host_machine_port> : <container_port>

10. To run the image as container with random port
    ~~~
    # docker  container run  -it  --name  <container_name>   -P  <img_name>
    ~~~

11. To run the image as container with hostname
    ~~~
    # docker container run -it --name <c_name> -h  <host_name>  <image_name>
    Ex: docker container run -it --name  ubuntu1 -h training ubuntu  
    ~~~
    
12. Run the command in container without attach to container
    ~~~
    # docker container exec  <cname> ls <path>
    Ex: # docker container exec ubuntu-cnt2 ls /etc/
    ~~~

13. Run the commands in container with root user without attach
    ~~~
    # docker container exec -u 0  <cname/cid> chmod -R <user_name>:<user_name> <path>
    Ex: # docker container exec -u 0 ubuntu-cnt2 chmod -R jenkins:jenkins  /var/jenkins_home/jobs
    ~~~
    ~~~
14. Attache the container with particular user
    ~~~
    # docker container exec -it <c_id> -u <user_name> /bin/bash 
    ~~~

15. Attache the container with root user
    ~~~
    # docker container exec -u 0 -it <c_id>  /bin/bash 
    ~~~
    
16. To display the Docker running Containers.
    ~~~
    # docker container ps 
    ~~~

17. To Display the last running container..
    ~~~
    # docker container ps -l
    ~~~

18. To Display the all the containers ether running or stop.
    ~~~
    # docker container ps  -a
    ~~~

19. To Display the particular number of the containers ether running or stop.
    ~~~
    # docker container ps -n 2
    ~~~

20. To stop the container
    ~~~
    # docker container stop  <cid>
    ~~~

21. To start the already existed container
    ~~~
    # docker container start  <cid>
    ~~~
22. To delete the images
    ~~~
    # docker rmi  <img_name>
    ~~~

23. To delete all the images
    ~~~
    # docker rmi  $(docker images -q)
    ~~~
 
24. To delete the container
    ~~~
    # docker rm  <cid>
    ~~~

25. To delete all the running container
  
    ~~~
    # docker rm  $(docker ps  -q)  --force
    ~~~

26. To delete all the container weather running or not
    ~~~
    # docker rm  $(docker ps  -a -q)  --force 
    or
    # docker container prune
    ~~~

27. to pause the processes in a running container.
    ~~~
    # docker  pause  <cid>  or  <cname>
    ~~~

28. to unpause the processes in a running container.
    ~~~
    # docker  unpause  <cid>  or  <cname>
    ~~~
29. To see the processes within a container
    ~~~
    # docker  top  <cid>  or  <cname>
    ~~~

30. to run a contaner with memory
    ~~~
    # docker run -d -m 300M centos
    ~~~

31. Show the history of an image
    ~~~
    # docker history <image_name>
    ~~~
    
32. Inspect changes to files or directories on a container’s filesystem
    ~~~
    # docker diff  <c_id>
    ~~~
    
33. To see the statistics of running containers
    ~~~
    # docker stats  <cid>
    ~~~

34. To see the full information of containers
    ~~~
    # docker inspect  <c_id>
    ~~~

35. Save one or more images to a tar archive
    ~~~
    # docker save -o  <tar_file_path> <image_name>
    ~~~

36. To know the logs of container
    ~~~
    # docker logs <c_id>
    ~~~

37. To check the continous logs of container
    ~~~
    # docker logs <c_id> -f
    ~~~

38. To know the docker information
    ~~~
    # docker system info
    ~~~

39. To change the container name
    ~~~
    # docker rename <old_name> <new_name>
    ~~~ 

40. To copy a file to container
    ~~~
    # docker container cp <file_path> <container_id>:<dest_path>
    ~~~ 

#### Connect db to container
1. run one db
    ~~~
    # docker run -d --name mydb -e MYSQL_ROOT_PASSWORD=root123 mysql
    ~~~
2. run one webapp container 
    ~~~
    # docker run -d --name wordpress2 --link mydb:mysql -p 90:80 wordpress
    ~~~
  
