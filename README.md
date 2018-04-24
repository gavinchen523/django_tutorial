# django_tutorial
<[Django tutorial](https://docs.djangoproject.com/en/2.0/intro/tutorial01/)>

###### Check Django version
    
`$ python -m django --version`

### Creating Project 
`$ django-admin startproject mysite`

### The development server
`$ python manage.py runserver`
    
### Creating the polls app
`$ python manage.py startapp polls`

### Wriet your first view
1. polls/views.py
2. polls/urls.py
3. mysite/urls.py  

`$ python manage.py migrate`  
`$ python manage.py runserver 0:8000`

### Creating models
1. Add database table to polls/models.py
2. Add pools to mysite/settings.py
3. create database table  
`$ python manage.py makemigrations polls`  
4. add polls to admin page(polls/admin.py)
5. test app<[localhost:8000](http://localhost:8000)>  
`$ python manage.py migrate`  
`$ python manage.py runserver 0:8000`

### Creating an admin user  
`python manage.py createsuperuser`  

    
