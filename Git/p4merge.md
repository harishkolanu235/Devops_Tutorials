** How to configure P4merge with git
---

difftool configuration
---
~~~
# git config --global diff.tool p4merge
# git config --global difftool.p4merge.path "C:\Program Files\Perforce\p4merge.exe"
# git config --global difftool.prompt false
~~~

mergetool configuration
---
~~~
# git config --global merge.tool p4merge
# git config --global mergetool.p4merge.path "C:\Program Files\Perforce\p4merge.exe"
# git config --global mergetool.prompt false
~~~
