# The Egel's Blog
> Simple, but heroic personal blog created in Django framework.

## Features:
  - Barebones styling - non CSS for now
  - Multi-categories and multi-tags for single post
  - Creating automatic slug in: post, category, tag
  - Auto-update the date of posts
  - [TinyMCE][1] editor
  - Based on Django 1.5.5

### Pages:
  - Single Post
  - Single Category
  - Single Tag
  - Posts -> Main wall
  - Categories
  - Tags
  - Archives

### TODO List
  - Add bootstrap 3 as main front-end framework
  - Python markdown syntax


## Instalation
Instalation is based on Ubuntu 14.04

  - pip + virtualenvwrapper

> All software for project is in the requirements.txt file

```bash
$ sudo apt-get install build-essential python-setuptools python-pip python-dev libmysqlclient-dev
$ sudo pip install --upgrade pip

$ sudo pip install virtualenvwrapper
```

Add some specific lines to the end of file `~/.bashrc`, for proper executing of virtualenvwrapper
```
# Settings for Virtualenvwrapper
export WORKON_HOME=$HOME/django_projects/virtualenvs
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh
```

Reload configuration and create virtualenv
```bash
$ source ~/.bashrc

$ mkvirtualenv myenv27 --no-site-packages
$ workon myenv27
(myenv27)$ cd ~/django_projects/virtualenvs/myenv27/
(myenv27)$ git clone git@github.com:egel/TheEgelBlog.git
(myenv27):~/django_projects/virtualenvs/myenv27$ pip install -r requirements.txt
```
Done, enjoy hacking :-)


## Run project

 - Create in local_settings.py (if is not)
 - Create mysql database (if is not)
 - Sync the project
 - Run :)

```
$ mysql -u root -p
mysql > CREATE database `django_theegelblog` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

$ workon myenv27
(myenv27)$ cd ~/django_projects/virtualenvs/myenv27/
(myenv27):~/django_projects/virtualenvs/myenv27$ python manage.py syncdb
(myenv27):~/django_projects/virtualenvs/myenv27$ ./manage.py runserver
```


## License
Software under [GNU AGPLv3](http://www.gnu.org/licenses/agpl-3.0.html) license.



  [1]: https://github.com/aljosa/django-tinymce
