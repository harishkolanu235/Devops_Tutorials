# Git Reset

git reset command is Just like a reset to defualt settings

There are two utilities of git reset command
1) To remove the changes from staging area
3) To undo the commits at repository level

---
1. To remove changes from staging area
    ~~~
    # git reset <file_name>
    
    Note: This command will bring changes from staging are to working directory, It is opposite to git add command.
    ~~~
    
2. To rmove files from only staging area back to working directory
    ~~~
    # git rm --cached <file_name>
    ~~~
