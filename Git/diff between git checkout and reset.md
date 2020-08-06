# git Checkout vs git reset

git checkout can be used to discard unstaged changes in working directory.

git reset can be used to discard staged changes from staging area.


# git rm --cached vs git reset

git rm --cached <file> ---> it will delete the file from staging area.
  
git reset <file> ---> The file wont be deleted from staging area, but reset to previous state (one step back)

