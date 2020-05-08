# Git Practicals
---
1. To create local repository
    ~~~
    # mkdir /gitlab
    # cd /gitlab
    # git init
    It will create .git directory. Where
    the .git directory is there that is local repository.
    # ls
    ~~~

2. How to add the file to Staging area
    ~~~
    # git add <file_name>
    ~~~

3. If you want to move all files to staging area
    ~~~
    # git add .
    ~~~

4. To see the status of a file
    ~~~
    # git status
    ~~~

5. To move a particular file from Stating space area to local repository
    ~~~
    # git commit -m "<commit_name>" <file_name>
    ~~~

6. If you want to commit all files to local repository
    ~~~
    # git commit -m "<commit_name>"
    ~~~

7. To see the commit messages?
    ~~~
    # git log 
    ~~~
8. To see the content of the commit?
    ~~~
    # git show <commit_number>
    # git log --oneline
    # git log --since=2018-01-21
    # git log --until=2018-03-18
    # git log --author="harishkolanu235"
    # git log --grep="index"
    # git log --oneline --author="harishkolanu235"
    # git log --oneline --name-only    ----> Show only names of changed files.
    # git log --oneline  --pretty=format:%h%x09%an%x09%ad%x09%s 
		%h ---> commit_id
		%x09 ---> space
		%an ----> author name
		%ad -----> date and time
		%s ----> commit message

    ~~~
   
9. To show the recent commit logs
    ~~~
    # git log -5
    ~~~

10. To see the difference between 2 commits
    ~~~
    # git diff <commit_id1>..<commit_id2>
    ~~~

11. To list of all branch
    ~~~
    # git branch

    Note: (*) represents your currently in that branch.
    ~~~

12. How to get back a commit to staging area?
    ~~~
    # git reset --soft HEAD^
    ~~~
    
13. How to get back a file from staging area to working area?
    ~~~
    # git reset head <file_name>
    ~~~
14. How to get back a commit to work area?
    ~~~
    # git reset --mixed <previous commit id>

    Note: We can get back first commit also but need repository default files commit Id
    ~~~

15. discard the latest commit perminately ?
    ~~~
    # git reset --hard HEAD^

    Note: if you want to discard the  latest 3 commits than use HEAD^^^ (or)  HEAD~3 
    ~~~
    or
    ~~~
    # git rebase -i HEAD^
    
    or
    
    # git rebase -i HEAD~3
    ~~~
    
16. When file have staging area or file have committed if file is deleted in local repository unfortunately how to get back that file to staging area?
    ~~~
    # git checkout -- <file_name>
    ~~~

17. To Create branch
    ~~~
    # git branch < branch_name >
    ~~~
18. Change the branch
    ~~~
    # git checkout <branch_name>

    Note: when newly or first-time checkout to branch, while checkout the committed files must copied from another branch to newly    checkout branch.
    Whenever checkout to another branch, Uncommitted files are copied to checkout branch evrytime.
    ~~~

19. To create a branch while switched to that branch
    ~~~
    # git checkout -b <branch_name>
    ~~~
20. To see the difference between 2 branches
    ~~~
    # git diff <branch1>..<branch2 >  
    ~~~
21. To delete the branch
    ~~~
    # git branch -d <branch_name>
    
    Note: if you want to delete forcefully, we can use below command
    # git branch -D <branch_name>
    ~~~
22. How do you push the files to master branch in remote repo?
    ~~~
    # git push (you must be in master branch)
    ~~~
23. How do you push files from local to particular branch in remote repo?
    ~~~
    # git push origin <branch_name>
    (or)
    # git push --set-upstream <branch_name>
    ~~~

24. How to push new branch and its data to remote repository?
    ~~~
    # git push <github_repository_path> <branch_name>
    (or)
    # git push --set-upstream <branch_name>
    ~~~
25. To Merge the branches
    ~~~
    # git merge <branch1> <branch2>
    
    Note: two diff content of the files
    ~~~
26. If you want to data move from branch1 to branch2
    ~~~
    # git merge <branch1>
    ~~~
    
27. How will you know in GIT if a branch has been already merged into master? 
    ~~~
    # git branch --merged   // It lists the branches that have been merged into the current branch. 
    # git branch --no-merged    // It lists the branches that have not been merged.
    ~~~
    
28. How to selectively pickup the commit's from child branch
    ~~~
    # git cherry-pick  <commit_id1> <commit_id2>
    
    Example:
    # git  cherry-pick   f29604a    efcb77a 
    
    ~~~

29. To store the data into stash? 
    ~~~
    # git stash save "<message>" 
    
    Note: the files must and should in the stage/index/cache area 
    ~~~
    
30. To see the stash list? 
    ~~~
    # git stash list
    ~~~
31. To copy the data into branches? 
    ~~~
    # git stash apply <stash#> 
    ~~~
32. To move the data into branches? 
    ~~~
    # git stash pop <stash#>
    ~~~
33. To delete the stash area?
    ~~~
    # git stash drop <stash#>   // delete the particular stash 
    # git stash clear       // delete the entire stash list
    ~~~
34. How to give an access to a specific person to repository? 
    ~~~
    You can invite users to become collaborators to your personal repository.
    • Under your repository, click on Settings.
    • In the left sidebar, click Collaborators.
    • Under "Collaborators", start typing the collaborator's username.
    • Select the collaborator's username from the drop-down menu.
    • Click Add collaborator.
    • The user will receive an email inviting them to the repository. Once they accept your invitation, they will have collaborator access to your repository.
    ~~~
35. How to Lock a branch? why we need to lock a branch?
    ~~~
    • On GitHub, navigate to the main page of the repository. 
    • Under your repository name, click on Settings. 
    • In the left menu, click on Branches. 
    • Select the branch you want to mark protected using the drop-down menu. 
    • Select Protect this branch. 
    • Click Save changes. 
    ~~~
36. How to delete Repository in GitHub?
    ~~~
    • On GitHub, navigate to the main page of the repository.
    • Under your repository name, click Settings.
    • Scroll to the bottom of the page and you will find Delete this repository button
    • When you click on that button, another pop up will appear, here you need to type in the name of your repository name and click on the button bellow which says: I understand the consequences, delete the repository.
    ~~~

33. To get the latest commit from all branches in remotely
    ~~~
    # for branch in `git branch -r | grep -v HEAD`; do git log --format=%h%x09%an%x09%ad%x09%s%x09%cr $branch -1 \\t$branch;done
    
    # for branch in `git branch -r | grep -v HEAD`; do echo $branch; git log --format=%h%x09%an%x09%ad%x09%s%x09%cr  $branch -1; echo -e "\n";done
    ~~~
34. To update all local branches
    ~~~
    # git pull --all
    ~~~
    
