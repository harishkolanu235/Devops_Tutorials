# Python Installation in Linux
---


1. First we need to install the required software dependencies that are all available in default CentOS repository.
    ##### If you are using CentOS
    ~~~
    # yum update
    # yum install gcc openssl-devel bzip2-devel libffi-devel python-devel mysql-devel -y
    ~~~
2. Download Python

3. Once the download is completed we have to extract the file from the downloaded Python Tar file. For that we will use Tar command.
    ~~~
    # tar -zxvf Python-3.7.7.tgz
    ~~~
    
4. Now let’s change the directory to Python.
Use below command
    ~~~
    # cd Python-3.7.7
    ~~~
    
5. We are in the source folder we can begin the source build process. For that first type below commands:
    ~~~
    # ./configure --prefix=/usr/local/python
    # make
    # make altinstall
    ~~~
    
6. Set the Python Path
    ~~~
    # echo "export PATH=/usr/local/python/bin:$PATH" >> /etc/profile
    # source /etc/profile        // update the file
    ~~~
    
7. 
    ~~~
    # ln -s /usr/local/python/bin/python3.7  /usr/local/python/bin/python3
    # ln -s /usr/local/python/bin/python3.7  /usr/bin/python3  
    ~~~
8. Check python version
    ~~~
    # python3 --version  
    ~~~

