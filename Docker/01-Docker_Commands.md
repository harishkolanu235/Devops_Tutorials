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
    # docker  run  -itd  --name <container_name>   <img_name>   
    Ex:  # docker  run  -d  --name  ubuntu_cnt2  ubuntu  
    ~~~

8. To entering the container
    ~~~
    # docker  attach  <cid> or <name>
    Ex: # docker attach ubuntu_cnt2
    ~~~
    *Note:* To exit the container as well as still runnig the container.
    press ctr + p + q

9. To run the image as container with port
    ~~~
    # docker  run  -it  --name  <container_name>   -p  81:80  <img_name>
    ~~~
    *Note:* -p <host_machine_port> : <container_port>

10. To run the image as container with hostname
    ~~~
    # docker run -it --name <c_name> -h  <host_name>  <image_name>
    Ex: docker run -it --name  ubuntu1 -h training ubuntu  
    ~~~
    
11. Run the command in container without attach to container
    ~~~
    # docker exec  <cname> ls <path>
    Ex: # docker exec ubuntu-cnt2 ls /etc/
    ~~~

12. Attache the container with particular user
    ~~~
    # docker exec -it <c_id> -u <user_name> /bin/bash 
    ~~~
13. To display the Docker running Containers.
    ~~~
    # docker  ps
    ~~~
	

14. To Display the all the containers ether running or stop.
    ~~~
    # docker  ps  -a
    ~~~

15. To stop the container
    ~~~
    # docker  stop  <cid>
    ~~~

16. To start the already existed container
    ~~~
    # docker start  <cid>
    ~~~
17. To delete the images
    ~~~
    # docker rmi  <img_name>
    ~~~

18. To delete all the images
    ~~~
    # docker rmi  $(docker images -q)
    ~~~
 
19. To delete the container
    ~~~
    # docker rm  <cid>
    ~~~

20. To delete all the running container
    ~~~
    # docker rm  $(docker ps  -q)  --force
    ~~~

21. To delete all the container weather running or not
    ~~~
    # docker rm  $(docker ps  -a -q)  --force 
    or
    # docker container prune
    ~~~

22. to pause the processes in a running container.
    ~~~
    # docker  pause  <cid>  or  <cname>
    ~~~

23. to unpause the processes in a running container.
    ~~~
    # docker  unpause  <cid>  or  <cname>
    ~~~
24. To see the processes within a container
    ~~~
    # docker  top  <cid>  or  <cname>
    ~~~

25. to run a contaner with memory
    ~~~
    # docker run -itd -m 300M centos
    ~~~

26. To see the statistics of running containers
    ~~~
    # docker stats  <cid>
    ~~~

27. To see the full information of containers
    ~~~
    # docker inspect  <c_id>
    ~~~

28. To know the logs of container
    ~~~
    # docker log <c_id>
    ~~~

#### Connect db to container
1. run one db
    ~~~
    # docker run -itd --name mydb -e MYSQL_ROOT_PASSWORD=root123 mysql
    ~~~
2. run one webapp container 
    ~~~
    # docker run -itd --name wordpress2 --link mydb:mysql -p 90:80 wordpress
    ~~~
  






    	

