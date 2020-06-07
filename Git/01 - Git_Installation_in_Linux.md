# Git Installation in Linux
---


1. First we need to install the required software dependencies that are all available in default CentOS repository.
    ##### If you are using CentOS
    ~~~
    # yum update -y 
    # yum groupinstall "Development Tools" -y
    # sudo yum install gettext-devel openssl-devel perl-CPAN curl-devel perl-devel zlib-devel -y
    # git --version
    ~~~
    ##### If you are using Ubuntu
    ~~~
    # apt-get update
    # apt-get install build-essential libssl-dev libcurl4-gnutls-dev libghc-zlib-dev zlib1g-dev tcl-dev libexpat1-dev gettext unzip
    ~~~
2. Download the latest git version.
   You will find the below link:
    [Download git](https://mirrors.edge.kernel.org/pub/software/scm/git/)
    ~~~
    # wget https://mirrors.edge.kernel.org/pub/software/scm/git/git-2.27.0.tar.gz
    ~~~
3. Once the download is completed we have to extract the file from the downloaded Git Tar file. For that we will use Tar command.
    ~~~
    # tar -zxvf git-2.27.0.tar.gz 
    ~~~
4. Now let’s change the directory to Git.
Use below command
    ~~~
    # cd git-2.27.0
    ~~~
5. We are in the source folder we can begin the source build process. For that first type below commands:
    ~~~
    # ./configure --prefix=/usr/local/git
    # make
    # make install
    ~~~
6. check the git version now, it wont change to new verison becasue we didn't set the path yet to new version
    ~~~
    # git --version
    ~~~
7. Set the Git Path, we have many ways to set the path. We can choose any one method.

    Method - 1) 
    ~~~
    # echo "export PATH=/usr/local/git/bin:$PATH" >> /etc/profile
    # source /etc/profile        // update the file
    ~~~
    Method - 2) 
    ~~~
    # vim /etc/profile.d/git.sh
        export PATH=/usr/local/git/bin:${PATH}
    # source /etc/profile.d/git.sh        // update the file
    ~~~
8. Now to check the version of Git, it has been changed.:
    ~~~
    # git --version
    ~~~

##### Configure the Github to our local
1. Configure your username and mail-id 
    ~~~
    # git config --global user.name "your_ name"
    # git config --global user.email "your_mail@example.com"
    ~~~
2. To confirm that whether  these configurations are added successfully or not.
    ~~~
    # git config --list
    ~~~
3. Now we need to generate a SSH key. SSH is a secure protocol used as the primary that means of connecting to linux servers remotely.
Now to generate a new SSH key we will use:
    ~~~
    # ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
    ~~~
4. Enable SSH Agent
    ~~~
    # eval "$(ssh-agent -s)"
    ~~~
5. Now we need add SSH key to the SSH agent we will use
    ~~~
    # ssh-add ~/.ssh/id_rsa
    ~~~
6. To See the SSH Key
    ~~~
    # cat ~/.ssh/id_rsa.pub
    ~~~
7. That Key add to your GitHub Account.
Open our GitHub Account go to settings under settings click on  SSH and GPG keys option on the left side.

8. We will click on New SSH key and add title and then paste the copied key in the space provided.
Now we will click on add SSH key
![screenshot](ssh.jpg)

9. Now use the below command to test the SSH key and press Enter after hit the below command.
    ~~~
    # ssh -T git@github.com
    ~~~
