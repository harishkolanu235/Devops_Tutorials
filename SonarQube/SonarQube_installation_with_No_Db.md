# SonarQube Installation

### Pre Requisite Softwares
    Java

### Hardware Requirements
    1. atleast 2GB RAM to run effeciently and 1GB of free RAM for the OS.

For Reference: **[https://docs.sonarqube.org/latest/requirements/requirements/](https://docs.sonarqube.org/latest/requirements/requirements/)**



### Installation
---
Login as root 

 ```
  $ sudo -i
 ```

Download Sonarqube server software
 ```
  $ cd /opt
  $ wget https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-9.1.0.47736.zip
  $ unzip sonarqube-developer-9.1.0.47736.zip
  $ mv sonarqube-developer-9.1.0.47736 sonarqube 
 ```

Note: As a good security practice, SonarQube server is not advice to run sonar service as root user. So create a new user called sonar.

Create a User
 ~~~
    $ adduser sonar
 ~~~

provide the sudo access to sonar user
 ~~~
    $ vim /etc/sudoers

    sonar   ALL=(ALL)   NOPASSWD:ALL
 ~~~

Change owner and group permission to /opt/sonarqube
 ~~~
    $ chown -R sonar:sonar /opt/sonarqube
 ~~~





  
