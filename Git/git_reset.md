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
          To discard the staged changes in staging area.
    ~~~
    
2. To remove files from only staging area back to working directory
    ~~~
    # git rm --cached <file_name>
    ~~~

Utility 2) To undo the commits at repository level

we can also reset to undo commits at repository level

Syntax:  git reset <mode>  <commit_id>

Note: Once you reset the commit, above commits also will be deleted
