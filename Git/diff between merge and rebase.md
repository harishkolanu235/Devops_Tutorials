# Difference between Merge and rebase


Merge

1. It is single step process.
  ~~~
  git checkout master
  git merge feature
  ~~~
2. Merge preserve history of all commits.
3. The commit can have more than one parent and hence history is non-linear
4. May be a chance of conflicts
5. We can aware which changes are coming from feature branch.


Rebase

1. It is a two-step process.
  ~~~
  git checkout feature
  git rebase master
  ~~~
2. rebase clears history of feature branch.
3. Every commit has a single parent, hence history is linear.
4. No chance of conflicts.
5. We can't aware which changes are coming. 




