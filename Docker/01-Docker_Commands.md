# Docker Commands
---

1. To Display the Docker Version.
   ~~~
    # docker  -v	
    or	
    # docker  --version
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

8. To entering the container
    ~~~
    # docker  attach  <cid> or <name>
    Ex: # docker attach ubuntu_cnt2
    ~~~
    *Note:* To exit the container as well as still runnig the container.
    press ctr + p + q

9. To run the image as container with specific port
    ~~~
    # docker  run  -it  --name  <container_name>   -p  81:80  <img_name>
    ~~~
    *Note:* -p <host_machine_port> : <container_port>

10. To run the image as container with random port
    ~~~
    # docker  run  -it  --name  <container_name>   -P  <img_name>
    ~~~

11. To run the image as container with hostname
    ~~~
    # docker run -it --name <c_name> -h  <host_name>  <image_name>
    Ex: docker run -it --name  ubuntu1 -h training ubuntu  
    ~~~
    
12. Run the command in container without attach to container
    ~~~
    # docker exec  <cname> ls <path>
    Ex: # docker exec ubuntu-cnt2 ls /etc/
    ~~~

13. Attache the container with particular user
    ~~~
    # docker exec -it <c_id> -u <user_name> /bin/bash 
    ~~~

14. To display the Docker running Containers.
    ~~~
    # docker container ps 
    ~~~

15. To Display the all the containers ether running or stop.
    ~~~
    # docker container ps  -a
    ~~~

16. To Display the particular number of the containers ether running or stop.
    ~~~
    # docker container ps -n 2
    ~~~

17. To stop the container
    ~~~
    # docker container stop  <cid>
    ~~~

18. To start the already existed container
    ~~~
    # docker container start  <cid>
    ~~~
19. To delete the images
    ~~~
    # docker rmi  <img_name>
    ~~~

20. To delete all the images
    ~~~
    # docker rmi  $(docker images -q)
    ~~~
 
21. To delete the container
    ~~~
    # docker rm  <cid>
    ~~~

22. To delete all the running container
  
    ~~~
    # docker rm  $(docker ps  -q)  --force
    ~~~

23. To delete all the container weather running or not
    ~~~
    # docker rm  $(docker ps  -a -q)  --force 
    or
    # docker container prune
    ~~~

24. to pause the processes in a running container.
    ~~~
    # docker  pause  <cid>  or  <cname>
    ~~~

25. to unpause the processes in a running container.
    ~~~
    # docker  unpause  <cid>  or  <cname>
    ~~~
26. To see the processes within a container
    ~~~
    # docker  top  <cid>  or  <cname>
    ~~~

27. to run a contaner with memory
    ~~~
    # docker run -d -m 300M centos
    ~~~

28. To see the statistics of running containers
    ~~~
    # docker stats  <cid>
    ~~~

29. To see the full information of containers
    ~~~
    # docker inspect  <c_id>
    ~~~

30. To know the logs of container
    ~~~
    # docker logs <c_id>
    ~~~

31. To know the comtinous logs of container
    ~~~
    # docker logs <c_id> -f
    ~~~

32. To know the docker information
    ~~~
    # docker system info
    ~~~

33. To change the container name
    ~~~
    # docker rename <old_name> <new_name>
    ~~~ 

34. To copy a file to container
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
  
