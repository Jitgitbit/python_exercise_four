pip3 install django
django-admin

REMOVING from git locally
1) (first remove it from github)
2) rm -rf <python-exercise-four>/.git   NOPE -->  in directory:   rm -rf .git
3) (now remove the directory itself too)

START:
django-admin startproject python_exercise_four

git init
git add .
git commit -m 'first'
gst
and then the github stuff...
git remote add origin git@github.com:Jitgitbit/python_exercise_four.git
git push -u origin master
gst
DONE

python3 manage.py startapp todo

python3 manage.py runserver
python3 manage.py migrate

python3 manage.py createsuperuser
thierrydekelver
django1234 (python3 manage.py changepassword username)

python3 manage.py makemigrations
python3 manage.py migrate


PYTHON ANYWHERE !!!
===================
------------------------
INSIDE Python Anywhere:
dashboard, bash
(linux-server)
ls
pwd
git clone https://github.com/Jitgitbit/python_exercise_four.git
ls
------------------------
INSIDE Python Anywhere:
dashboard, bash
(linux-server)
ls
cd python_exercise_four
mkvirtualenv --python=/usr/bin/python3.8 todowoovenv
python
exit()
deactivate
cd .virtualenvs/
ls
cd ..
workon todowoovenv
pip install django pillow
-----------------------
INSIDE Python Anywhere:
dashboard, bash
(linux-server)
ls
cd python_exercise_three/
pwd
ls

OPEN UP NEW TAB
INSIDE Python Anywhere:
web, +add a new web app (domain name www.todowoo.info), next, Manual configuration, next, Enter path to a virtualenv, if desired :
portfoliovenv
Enter the path to your web app source code :
/home/thierryD/python_exercise_four
Go to directory
python_exercise_four/
settings.py
DEBUG = False
ALLOWED_HOSTS = ['www.todowoo.info']
HIT SAVE
CLICK ON PYTHONLOGO (left corner) to go back, web, HIT Reload www.todowoo.info
Working directory:
/home/thierryD/python_exercise_four

INSIDE WSGI configuration file:

ONLY LEAVE:
# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
#import os
#import sys
#
## assuming your django settings file is at '/home/thierryD/mysite/mysite/settings.py'
## and your manage.py is is at '/home/thierryD/mysite/manage.py'
#path = '/home/thierryD/mysite'
#if path not in sys.path:
#    sys.path.append(path)
#
#os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
#
## then:
#from django.core.wsgi import get_wsgi_application
#application = get_wsgi_application()


AND THEN:
import os
import sys

# assuming your django settings file is at '/home/thierryD/mysite/mysite/settings.py'
# and your manage.py is is at '/home/thierryD/mysite/manage.py'
path = '/home/thierryD/python_exercise_four'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'python_exercise_four.settings'

# then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

HIT SAVE
CLICK ON PYTHONLOGO (left corner) to go back, web, HIT Reload www.todowoo.info
========================================================================
========================================================================
========================================================================
========================================================================
========================================================================
========================================================================
========================================================================
========================================================================
========================================================================
========================================================================
========================================================================

OPEN UP NEW TAB
thierryD.pythonanywhere.com
--------------------------------
INSIDE Python Anywhere:
dashboard, bash
(linux-server)
ls
python manage.py collectstatic
ls 
cd static
pwd

IN OTHER TAB
INSIDE Python Anywhere:
web, Enter URL:
/static/
Enter path:
/home/thierryD/python_exercise_three/static
add another one: Enter URL:                   -----> this is needed because DEBUG = False
/media/
Enter path:
/home/thierryD/python_exercise_three/media

HIT Reload thierryD.pythonanywhere.com
cmd+shift+r (hard reload)
----------------------------------------
INSIDE Python Anywhere:
web, Force HTTPS: Enabled

HIT Reload thierryD.pythonanywhere.com
----------------------------------------
INSIDE Python Anywhere:
dashboard, bash
(linux-server)
ls
cd python_exercise_three/
workon portfoliovenv

git status
nano .gitignore

*.log
*.pot
*.pyc
__pycache__/
local_settings.py
/static/

ctrl+x
y
HIT enter
git status
git add .gitignore
git status
git commit -m "Added a gitignore via PythonAnywhere"
git config --global user.email "mail-address@mail.com"
git config --global user.name "your name"
git commit -m "Added a gitignore via PythonAnywhere"
git status
git rm -r --cached .
git add .
git commit -m "removed old stuff"
git status
git pull origin
git push origin
"So don't forget to keep them in sync both locally and on github now !!!"
----------------------------------------
exiting console: type exit
exiting VIM: type :qa! HIT enter
------------------------------------
pip3 freeze > requirements.txt (in regular terminal)
------------------------------------
cmd+ctrl+space (adding emoji)
INSIDE Python Anywhere:
dashboard, bash
(linux-server)
ls
cd python_exercise_three
workon portfoliovenv
git pull origin
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic
yes (overwrite?)
after commit:
git pull origin
INSIDE Python Anywhere:
web, HIT Reload thierryD.pythonanywhere.com
-----------------------------------