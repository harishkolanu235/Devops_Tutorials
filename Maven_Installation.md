# Maven Installation in Centos
---


1. Download the latest maven from https://maven.apache.org/download.cgi
    ~~~
    $ cd /opt/
    $ wget https://mirrors.estointernet.in/apache/maven/maven-3/3.8.1/binaries/apache-maven-3.8.1-bin.tar.gz
    $ tar -zxvf apache-maven-3.8.1-bin.tar.gz
    ~~~

2. Set the PATH for Maven
    ~~~
    $ vim /etc/profile.d/maven.sh
        export M2_HOME=/opt/apache-maven-3.8.1
        export PATH=${M2_HOME}/bin:${PATH}
    ~~~

3. Update maven.sh file to kernal
    ~~~
    $ source /etc/profile.d/maven.sh
    ~~~
    


