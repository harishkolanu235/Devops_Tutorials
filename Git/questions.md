#### 1. What is GIT? 

    GIT is a distributed version control system and source code management (SCM) system with an emphasis to handle small and large projects with speed and efficiency.  

#### 2. What is Distributed Control System? 
    We work in our local machine and later we transfer the code to Centralized repository 
(GitHub). We don’t need to connect to centralized repository to work. 

#### 3. What is GIT version control?  
    -  GIT version control allows you to track the history of a collection of files (code files). 
    - It supports creating different versions of file collection. Each version captures a snapshot of the files at a certain point of time and You can revert the collection of files using the snapshot. (You can develop the code in different versions of java. and you can merge in Git) 
    - VCS allows you to switch between these versions. These versions are stored in a specific place, typically called as repository. (You can switch between different versions of java in between development process) 

### 4. What is difference between SVN and Git?  
|SVN | GIT |
|----|-----|
| SVN is centralized repository, that means directly we involved in the centralized repository | Git is distributed repository, first we are  working in our laptop after that we are transferring the code from our laptop to  centralized repository. Git have three phases the phases are work space, staging/index, local repo.| 
| If we are facing any network issue, we can’t work on SVN because of we are directly involve into the centralized repository. |In git we are doing in local systems only so no need to internet connection, when pushing the code from our system to centralized repository at that time we need network connection. Without network also, we can do some work. |
| Developed directly interact with the centralized repository.| Developers not directly interact with the Centralized repository. |
| SVN is much easier to learn. | GIT is a bit difficult to learn for some developers, it has more concepts and commands to learn.|
| SVN can handle large binary files easily.| GIT becomes slow when it deals with large binary files that changes frequently. |
| SVN has good user interface. | GIT does not have good UI.|
| SVN create .svn directory in each directory. | GIT creates only .git directory. 
 
#### 5. What is a repository in GIT?  
    A Git repository contains the history of a files.  
#### 6. How can you create a local repository in Git?  
    By using # git init command create a local repository. 
#### 7. What is ‘bare repository’ in GIT?  
    .git directory in repository is called as bare repo. A bare repository in Git just contains 
the version control information and no working files (no tree) and it doesn’t contain the 
special .git sub-directory.  
#### 8. How to configure GitHub repository locally? 
    $ git config --global user.name "user_name"  
    $ git config --global user.email "user_email" 
#### 9. How to remove/unset a user?  
    $ git config --global --unset user.name  
    $ git config --global –unset user.email 
    $ git config –global –unset-all user.name 
#### 10. How to Create Alias to git commands 
    $ git config --global alias.lo "log --oneline" -----> To create an Alias to Command 
    $ git config --global --unset alias.lo  -----> To Remove an Alias      
#### 11. What is the git clone?   
    To download an existing repository from Centralized (Github) to local system. 
    $ git clone <url> 
#### 12. What is ‘git add’? 
    To add files from work area to Index/staging/cache area.  
    $ git add <file_name1> <file_name2> 
#### 13. What is Staging Area?  
    staging area means “holding area”. Before the commits, it can be formatted and reviewed in an intermediate area known as staging or Index Area. 
#### 14. What is the use of ‘git log’?  
    To see the commits. Also, we can find specific commits in your project history- by author, date, content or history. 
    $ git  log  -----> To show the Git Commits
    $ git  log   -5   -----> To show Recent 5 Commits 
    $ git log –grep=”commit id”  → To see a particular commit 
    $ git log –grep =”commit id 2” –grep=”commit id 5” ----> To see particular commits among all 
    $ git  log    --oneline -----> To Display the each commit in one line 
    $ git  log   --since=2018-01-21 
    $ git  log   --until=2018-03-18 
    $ git  log   --author="user_name" 
    $ git  log   --grep="Index" 
    $ git  log   --oneline   --author="user_name" 
#### 15. How can we add modified/updated/edited files to the staging area and commit then at the same time? 
    $ git  commit  -a  -m  "<commit-name>" <filename> 
    Note: The file must be committed at least once. 
#### 16. How to edit an incorrect commit message in Git?  Or How can you fix a broken commit? Or How can you change a commit name? 
    $ git  commit –amend (you must be on the commit(head)) or  
    $ git commit  --amend  -m  "New name for commit" (you must be on the commit(head)) 
#### 17. How to get back a commit to staging area? 
    $ git  reset  --soft  <previous_commit id> 
    It removes/clears the commit history of particular commit. 
#### 18. How to get back a commit to work area? 
    $ git  reset  --mixed  <previous commit id> 
    It removes/clears the commit history of particular commit. 
#### 19. How to get back a file from staging area to working area? 
    $ git  reset  head  <file_name> 
#### 20. What is git reset? 
    Reset the current HEAD state to specific state. 
#### 21. How do you reset current branch state to previous state? 
    $ git reset –hard 
    Git reset –hard HEAD clears the mess from the index file and the working tree. (doesn’t impact on untracked files) 
    Or 
    (It resets the working tree (working and staging areas) to last commit) 
#### 22. How do you undo the last commit? 
    $ git revert <commit id> 
It keeps the commit history and creates another commit (‘revert commit’) 
23. What is ‘head’ in git and how many heads can be created in a repository? 
A ‘head’ is simply a reference to a commit object. In every repository, there is a default 
head referred as “Master”.  A repository can contain any number of heads. 
24. What is .gitignore file? 
Keep the files names in .gitignore then that files not add and commit, just skip that files 
while adding and committing. 
25. How to see the difference between 2 commits? 
    $ git  diff  <commit_id1>..<commit_id2> 
#### 26. How do you get back a deleted file in local repository (work area) which is not staged or committed at least once? 
    Not possible. Can’t get back. 
#### 27. How do you get back a deleted file in local repository (work area) which is already staged? Or How do you get back a deleted file in local repository (work area) which is already committed?
    $ git checkout -- <file name> 
#### 28. How to create a branch? 
    $ git branch <branch name> 
#### 29. How to checkout from one branch to other? 
    $ git checkout <branch name> 
#### 30. How to create branch and checkout at the same time? 
    $ git checkout -b <branch name> 
#### 31. How do you rename the local branch? 
    $ git  branch  -m  <old_branch_name> <new_branch_name> 
#### 32. How to see the branch list? 
    $ git branch  
#### 33. How to see the remote branch list? 
    $ git  branch  -r 
    Or 
    $ git  remote   show   origin 
#### 34. How to see the local and remote branch list? 
    $ git  branch  -a 
#### 35. How to delete a branch? 
    $ git  branch   -d  <branch_name> 
    Or 
    $ git  branch  -D   <branch_name> 
#### 36. How to delete a Remote Branch?  
    $ git  push origin  -d  <branch_name> 
    Or 
    $ git push origin : <branchname> 
#### 37. How to see the difference between 2 branches 
    $ git diff <branch1>..<branch2 > 
#### 38. What is git push?  
    git push is to push commits from your local repository to a remote repository.  
#### 39. How do you push the files to master branch in remote repo? 
    $ git push  (you must be in master branch) 
#### 40. How do you push files from local to particular branch in remote repo? 
    $ git push origin <branch_name>  
    (or) 
    $ git push --set-upstream <branch_name> 
#### 41. How to put/push a local repository to GitHub? 
    ~~~
    $ git remote add origin <remote_repository_URL>

    Process:
    - Create a new repository on GitHub. Do not initialize the new repository 
    with README, license, or gitignore files. You can add these files after your project 
    has been pushed to GitHub. 
    - Open Git Bash. 
    - Change the current working directory to your local project. 
    - Initialize the local directory as a Git repository.
        $ git init 
    - Add the files in your new local repository. This stages them for the first commit. 
    To unstage a file, use $ git reset HEAD  <your_filename>  
        $ git add . 
    - Commit the files that you've staged in your local repository. 
        $ git commit -m “First commit” 
    - At the top of your GitHub repository's Quick Setup page, click  to copy the remote 
    repository URL. 
    - In the Command prompt, add the URL for the remote repository where your local 
    repository will be pushed. 
        $ git remote add origin <remote_repository_URL> 
    - verify the new remote URL 
        $ git remote -v 
    - Push the changes in your local repository to GitHub. 
        $ git push origin master  
    ~~~
#### 42. How to push new branch and its data to remote repository? 
    $ git push origin <branch name> Or 
    $ git push -u origin <branch name> Or 
    $ git push -u origin <branch name>:<branch name> 0r
    $ git push --set-upstream <repo url> <branch_name> 
#### 43. What is git pull? 
    - Git pull downloads and merges a ‘branch data’ from remote repository to local repository. 
    - It may also lead to ‘merge conflicts’ if your local changes are not yet committed. Use ‘git  stash’ command to Hide your local changes before git pull. 
    $ git pull  (git fetch + git merge.) 
#### 44. How do you pull a file from particular remote branch? 
    $ git pull origin <branch_name> 
#### 45. How do you download a remote branch to local without merge? Or how-to checkout remote branch? Or How to get a remote branch to local? Or How to checkout a remote branch? 
    $ git fetch origin <branch_name>     (downloads the remote branch.) 
    (and) 
    $ git checkout  <downloaded_branchname> (merges the downloaded branch with local) 
#### 46. What is git Fetch?  
    git fetch only downloads new data from a remote repository, but it doesn’t integrate any of the downloaded data into your working files. All it does is provide a view of this data. 
    $  git  fetch   <branch_name> 
    $ git  fetch  origin  <branch_name>  
#### 47. What is difference between git clone & git pull? 
    - If you want to download whole existing repository than use Git Clone.  
    - If you have already repository but you want to take new updates of existing repository than use git pull command. 
#### 48. What is difference between git clone and git remote?  
    - Git clone is used to create a new local repository whereas git remote is used in 
existing repository. 
    - Git clone create a new local repository by copying another repository from a URL. Git remote adds a new reference to existing remote repository for tracking further changes. 
#### 49. What is git merge?  
    Git merge is used to combine two branches. 
    $ git merge <branch_name> 
    Note: you should be in target branch. Then run the command 
#### 50. What is git conflict? What is the scenario you will get git conflict error? 
    For example, if you and another person both edited the same file on the same lines in different branches of the same Git repository, you'll get a merge conflict error when you try to merge these branches. You must resolve this merge conflict with a new commit before you can merge these branches. 
#### 51. How do you resolve merge conflict? 
    we Will inform the developers regarding this merge conflict. They will change the code and inform us. edit the files to fix the conflicting changes and then add & commit. 
#### 52. How do you skip from merge conflict? 
    $ git merge --abort 
#### 53. What is the function of ‘git rm’?  
    To remove the file from the work area/staging area and also from your disk ‘git rm’ is used. You can revert a deleted file. if it is deleted using ‘git rm’. If you deleted a file ‘rm’ command then you can’t get it. 
#### 54. How will you know in GIT if a branch has been already merged into master?  
    $ git branch -merged ---> It lists the branches that have been merged into the current branch. 
    $ git branch -no-merged ---> It lists the branches that have not been merged. 
#### 55. What is branching? What is the purpose of branching in GIT?  
    Git supports branching which means that you can work on different versions of your collection of files. A branch allows the user to switch between these versions so that he can work on different changes independently from each other. 
#### 56. What is the criteria u merge two branches? 
    We have developed one module in one branch and another module in another branch. After the development, based on the requirement we do merge these two branches. Or One branch is development branch, another branch is test branch. 
#### 57. Describe branching strategy you have used? 
    Feature branching 
        A feature branch model keeps all of the changes for a particular feature inside of a branch. When the feature is fully tested and validated by automated tests, the branch is then merged into master. 

    Task branching 
        In this model each task is implemented on its own branch with the task key included in the branch name. It is easy to see which code implements which task, just look for the task key in the branch name. 

    Release branching 
        Once the develop branch has acquired enough features for a release, you can clone that branch to form a Release branch. Creating this branch starts the next release cycle, so no new features can be added after this point, only bug fixes,documentation generation, and other release-oriented tasks should go in this branch.Once it is ready to ship, the release gets merged into master and tagged with a version number. In addition, it should be merged back into develop branch, which may have progressed since the release was initiated. 
#### 58. What is git stash? 
    Stashing takes the Temporary stored state of your working directory. 
    $ git  stash  save  "<message>" ------> to store the data into stash 
    $ git  stash list  ------> to see the stash list
    $ git  stash apply  <stash#> ------> to copy the data into branches 
    $ git  stash pop  <stash#> ------> to move the data into branches 
    $ git  stash drop  <stash#> ------> to delete the particular stash
    $ git  stash clear  ------> delete the entire stash list
#### 59. When we use git Stash?     
    - Sometimes we don’t want to commit some files and we don’t want to lose also that files. That files may be unfinished files. In this case we use git stash command  
    - If you are checking out from one branch to another branch but you have uncommitted file that you don't want to move then keep that file in stash area. 
    - When you are merging two branches and you don't want some files to merge, then we move that files to stash area. 
    - When you are pulling (fetch + merge) a branch/file and you don't want some files to merge, then we move that files to stash area. 
#### 60. What is another option for merging in git? 
    $ git rebasing command is an alternative to merging in git. 
#### 61. What is difference between git merge and git rebase? 
    - git merge applies all unique commits from branch A into branch B in one commit with final result. 
    - git rebase gets all unique commits from both branches and applies them one by one. 
    - git merge doesn’t rewrite commit history, just adds one new commit 
    - git rebase rewrites commit history but doesn’t create extra commit for merging 
#### 62. How to Change the URL for a remote Git repository? 
    #  git  remote   set-url   origin   git://this.is.new.url 
#### 63. What is pull request? 
    Take some changes from a particular branch and bring them into another branch.  
#### 64. Why GIT better than Subversion (SVN)? 
    Git is an opensource version control system; it will allow you to run ‘version' of a project. Multiple developers can check out, and upload changes and each change can then be attributed to a specific developer. 
#### 65. How to delete Repository in GitHub? 
    - On GitHub, navigate to the main page of the repository. 
    - Under your repository name, click Settings. 
    - Scroll to the bottom of the page and you will find Delete this repository button 
    - When you click on that button, another pop up will appear, here you need to type in the name of your repository name and click on the button bellow which says: I understand the consequences, delete the repository. 
#### 66. how to give an access to a specific person to repository? 
    - You can invite users to become collaborators to your personal repository. 
    - Under your repository, click on Settings. 
    - In the left sidebar, click Collaborators. 
    - Under "Collaborators", start typing the collaborator's username. 
    - Select the collaborator's username from the drop-down menu. 
    - Click Add collaborator. 
    - The user will receive an email inviting them to the repository. Once they accept your invitation, they will have collaborator access to your repository. 
#### 67. How to lock a branch? Why we need to lock a branch? 
    - On GitHub, navigate to the main page of the repository.  
    - Under your repository name, click Settings.  
    - In the left menu, click Branches.  
    - Select the branch you want to mark protected using the drop-down menu.  
    - Select Protect this branch. 
    - Click Save changes. 
#### 68. What is cherry pick? 
    To get a particular commit from one branch to other. Or  
    To get a particular file from one branch to another branch. Or 
    To merge a particular file from branch to another branch. 
    $ git cherry-pick <commit-id> 
#### 69. What is squash? 
    Squashing a commit means, simply making two commits into one commit or Combining commits. If you repeat this process multiple times, you can reduce n commit to a single one. 
#### 70. How to check the parent commit? 
    $ git cat-file -p <commit-id> or 
    $ git cat-file -p <tree id (#code/ sha code)> 
    $ git-cat-file --->Provide content or type and size information for repository objects. 
#### 71. How can you add only modified files to staging area (only modified files (tracked files) but not untracked files)? 
    $ git add -u 
#### 72. How do you check your git push is success or not? 
    $ git ls-remote <branchName> 

