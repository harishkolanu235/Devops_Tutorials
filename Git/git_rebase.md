# Git Rebase

Git rebase is two step process

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

##### Advantages of git reabase 

1. git rebase keeps history clean.
   Every commit has a single parent.

2. Clear work flow(linear) will be there. Easy to understand for the developers.
3. Fast-Forward merge, no chance of conflicts.
4. No extra commit like merge commit.

##### Disadvantages of git reabase 

1. It rewrite history. we can't see history of commits from feature branch.
2. We doen't aware which chnages are coming from feature branch. 

  ~~~
  Note: Rebase is very dangerous operation and it is never recommended  to use on public repositories because it rewrite history.
  ~~~
