# diff between fast-forward and 3 way merge

fast-forward 

1) after creating child branch, only child branch is modified, parent branch is not modified.
2) it doesn't require any new commit.
3) No chance of conflict
4) It is fully handled by git.

3-way 

1) after creating child branch, both child and parent branch is updated.
2) A new commit will be created, which is known as merge commit
3) may be a chance of conflict
4) If there is conflict, we have to handle manually.
