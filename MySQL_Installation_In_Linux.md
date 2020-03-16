# MySQL Installation in Linux
---


1. Download MySQL, You will find the below link:
    ~~~
    https://dev.mysql.com/downloads/repo/yum/
    # wget https://dev.mysql.com/get/mysql57-community-release-el7-9.noarch.rpm
    ~~~
 
2. Install the MySQL
    ~~~
    # rpm -ivh mysql57-community-release-el7-9.noarch.rpm
    # yum install mysql-server -y
    ~~~
    
3. Start the MySQL
    ~~~
    # systemctl start mysqld
    # systemctl status mysqld
    # systemctl enable mysqld
    ~~~
    
4. During the installation process, a temporary password is generated for the MySQL root user. Locate it in the mysqld.log with this command:
    ~~~
    # grep 'temporary password' /var/log/mysqld.log
    ~~~
    ~~~
    Output
    2016-12-01T00:22:31.416107Z 1 [Note] A temporary password is generated for root@localhost: mqRfBU_3Xk>r
    ~~~
    
 5. Configuring MySQL
    ~~~
    # mysql_secure_installation
    ~~~
    ~~~
    Output
    The existing password for the user account root has expired. Please set a new password.

    New password:
    ~~~
    
 6. Testing MySQL
    ~~~
    # mysqladmin -u root -p version
    ~~~
 
    
    
