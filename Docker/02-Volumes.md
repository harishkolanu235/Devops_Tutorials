# Docker Volumes step by step 

#### Use of Volumes
1. Decoupling container from storage
2. Share volume (storage/data) among diffrent contaners
3. Attache volume to container 
4. Once deleting container, volume does not delete.

#### Basic commands for docker volumes
1. To get the information of volumes
   ~~~
   docker volume 
   ~~~
2. To Create a volume
   ~~~
   docker volume create <volume_name>
   ~~~
3. To See the list of volumes
   ~~~
   docker volume ls
   ~~~
4. To See the description of volume
   ~~~
   docker volume inspect <volume_name>
   ~~~
5. To remove a volume
   ~~~
   docker volume rm <volume_name>
   ~~~
6. To remove all the volumes
   ~~~
   docker volume prune
   ~~~

#### How to attache volume to container
   ~~~
   docker run -d --name myJenkins1 -p 9090:8080 -v <volume_name>:/var/jenkins_home jenkins 
   ~~~

*Note:*  Delete container and check your volume data, it does not remove. 

#### To share a volume or an directory to container
   ~~~
   # docker run -it --name ubuntu3 -v /opt/test:/opt/ubuntu
   ~~~

#### To share a volume from one container to another
   ~~~
   # docker run -it --volumes-from <c_id> ubuntu
   ~~~
