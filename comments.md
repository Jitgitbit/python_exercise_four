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