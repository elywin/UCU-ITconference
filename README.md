# UCU-ITconference
A conference management system in Django

**https://ucuitconference.herokuapp.com/**

# Poject setup

- Clone the project: `git clone https://github.com/elywin/UCU-ITconference.git`
- Change directory: `cd UCU-ITconference`
- Create virtual environment: `python  -m venv env`
- Activate the environment: `source env/bin/activate` (linux/unix)
- Install dependencies: `pip install -r requirements.txt`
- Register models: `python manage.py makemigrations`
- Create database: `python manage.py migrate`
- Create superuser: `python manage.py createsuperuser` (for the admin use)
- Run web app: `python manage.py runserver`  (http://127.0.0.1:8000/)
