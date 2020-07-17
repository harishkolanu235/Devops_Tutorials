# Git Remove
---
1. To remove files from both working directory and staging area
    ~~~
    # git rm <file_name>
    
    Note: git always compare from right to left side, means git diff <file_name> command compare from staging area to working area.
    ~~~
    
2. To rmove files from only staging area but not from working directory
    ~~~
    # git rm --cached <file_name>
    ~~~
    
3. To remove files from working directory 
    ~~~
    # rm <file_name>
    ~~~
    
4. To remove all files from working directory 
    ~~~
    # git rm -r .
    ~~~
