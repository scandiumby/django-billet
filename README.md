# django-billet
Blank Django project on docker container with Bootstrap and SB Admin connected

## How to create new project by django-billet
1. Clone git@github.com:scandiumby/django-billet.git
1. Remove .git folder in project
1. Rewrite content of `title` and `h1` blocks in *core/templates/core/pages/home.html*
1. Rewrite project name (see html tag `div` with `sidebar-brand-icon class`) 
in *core/templates/core/base-with-sidebar.html*
1. Change port from `8000` (see web/command and web/ports sections)
to any other valid if needed in *docker-compose.yml* and *dev.env*
1. Change database name from `djangobillet` to name which you like in *docker-compose.yml* (see POSTGRES_DB) and 
*dev.env* (see end of DATABASE_URL)
1. go to project folder by terminal and execute `make i`
1. If you have error with allocate 5432 port for postgres then you will change first number in postgres/ports to any other
1. Go to 0.0.0.0:[port from 5 or 8000] in your prefer browser and develop!
1. Good luck!

### How to configure origin to github and pushing first commit
1. go to project folder by terminal
1. `git init`
1. `git add -v .`
1. `git commit -m "init commit"`
1. `git branch -M master`
1. `git remote add origin [link to github repo]`
1. `git push -u origin master` 


