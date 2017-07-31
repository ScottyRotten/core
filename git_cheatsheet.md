## How to Contribute to a Project (FORK)

http://kbroman.org/github_tutorial/pages/fork.html

## How to Keep a Fork Updated

https://www.sapien.com/blog/2016/05/16/github-how-to-update-your-fork/

First Time: Link to the original source

1) List remotes: git remote -v
2) Add original project to remotes: git remote add <name> <copiedURL>

git fetch <nameOfRemote>
git merge <nameOfRemote>\<branch> (master)


## Workflow

git status ;checks if you have most current files
git pull ;downloads most upto date files
git add . ;Stages changes Adds all changes you made or . can be replaced with a single files name
git commit -m "your comment here" ;commits changes that were added to repository (Local Copy)
git push ;Uploads most recent changes to github server
git push origin master ; Pushes to forked repo
git rm ;remove git files, follow with commit and push
