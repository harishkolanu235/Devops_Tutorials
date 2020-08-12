# Git Rebase

##### Git rebase is two step process

1. Rebase feature branch on top of master branch.
  ~~~
    # git checkout feature
    # git rebase master
  ~~~
2. Merge feature branch into master branch (fasr-forwad merge)
  ~~~
    # git checkout master
    # git rebase feature
  ~~~

Advantages of git reabase 

1. git rebase keeps history clean.
   Every commit has a single parent.

2. Clear work flow(linear) will be there. Easy to understand for the developers.
3. Fast-Forward merge, no chance of conflicts.
4. No extra commit like merge commit.

Advantages of git reabase 

1. 
