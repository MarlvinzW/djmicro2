# Django Microservices Template

Includes:

01. Django
02. Django REST Framework
03. MongoDb ORM
04. Celery
05. Docker
06. Swagger API Docs

Steps:
01. Install Cookiecutter: ```python pip install cookiecutter ```
02. Startproject: ```python cookiecutter gh:cyantarek/djmicro2 ```
03. Answer questions and give your service a name
04. cd into the folder
05. Install requirements: ```python pip install -r requirements.txt ```
06. Run server: ```python python manage.py runserver ```
07. Run celery: ```python celery -A api workder -l info ```
08. Start rabbitmq, mongodb and configure them in settings.py
09. Create Celery tasks in tasks.py
10. Hello World API endpoint: ```python 127.0.0.1:8000/api/v1/hello/ ```
11. Swagger API Docs endpoint: ```python 127.0.0.1:8000/api/v1/docs/ ```
