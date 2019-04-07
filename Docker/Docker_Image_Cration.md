# Docker Image Creation
Below are some dockerfile commands you must know:

1. ###### FROM
    The base image for building a new image. This command must be on top of the dockerfile.

2. ###### MAINTAINER
    Optional, contains the name of the maintainer of the image.

3. ###### RUN
    Used to execute a command during the build process of the docker image.

4. ###### ADD
    Copy a file from the host machine to the new docker image. There is an option to use an URL for the file, docker will then download that file to the destination directory.

5. ######   ENV
    Define an environment variable.

6. ######   CMD
    Used for executing commands when we build a new container from the docker image.

7. ###### ENTRYPOINT
    Define the default command that will be executed when the container is running.

8. ###### WORKDIR
    This is directive for CMD command to be executed.

9. ###### USER
    Set the user or UID for the container created with the image.

10. ###### VOLUME
    Enable access/linked directory between the container and the host machine.
