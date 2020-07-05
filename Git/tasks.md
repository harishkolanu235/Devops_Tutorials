# Git Difference
---
1. To see the difference in file content between working directory and staging area
    ~~~
    # git diff <file_name>
    
    Note: git always compare from right to left side, means git diff <file_name> command compare from staging area to working area.
    ~~~
    
2. To see the difference in file content between working directory and last commit
    ~~~
    # git diff HEAD <file_name>
    
    Note: 
    latest commit can be referenced by HEAD
    HEAD ---> latest commit
    ~~~
    
3. To see the difference in file content between working directory and sepecific commit
    ~~~
    # git diff <specifi_commit> <file_name>
    ~~~
    
4. To see the difference in file content between staging area and last commit
    ~~~
    We have to use --staged or --cached option
    # git diff --staged HEAD <file_name>
    or
    # git diff --staged <file_name>
    
    Note: if you dont mention HEAD, it will take by defualt it takes right side area means it takes HEAD.
    Example: # git diff <file_name> ---> here dont mention HEAD so by defualt it takes right side area means staging area, so it compare to staging area to working area.
    ~~~
    
5. To see the difference in file content between staging area and specifi commit
    ~~~
    # git diff --staged <specific_commit> <file_name>
    ~~~
    
6. To see the difference in file content between two commits.
    ~~~
    # git diff <commit1>..<commit2>
    ~~~
7. Last commit vs last but one commit
    ~~~
    # git diff HEAD HEAD~1
    
    or
    
    # git diff HEAD HEAD^1
  
    
    Note: if you want compare with perticular file
    # git diff HEAD HEAD~1 <file_name>
    or 
    # git diff HEAD HEAD^1 <file_name>
    ~~~
   
 8. To see the difference in content of between two branches
    ~~~
    # git diff <branch1> <branch2>
    ~~~
 
9. To see the difference in local repository and remote repository
    ~~~
    # git diff master origin/master
    ~~~
