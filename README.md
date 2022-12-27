# DjangoToDoAPI
Project using Django rest framework to create REST api for ToDo list application with user registration

## Installation
1. install python3 from <a href="https://www.python.or
g/" target="_blank">here</a> 
2. pip install -r requirements.txt
3. install postgreSQL
4. create database in postgreSQL
5. Configure the database in Settings.py as per below code snipper
  ```
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '<databasename>',
        'USER': '<owner of database>',
        'PASSWORD': '<password for owner of DB>',
    }
    }
   ```
6. python manage.py makemigrations
7. python manage.py migrate
8. python manage.py runserver
---
# api paths
## api/v1/
### api/v1/signup/
**Allowed Methods** : POST
<br>**Access Level** : Public
<br>**fields :** 'required': {"email","password"} Details: email - Used for login and should be unique, password - Used for login
<br>On successfull request, user details will be returned.
<br>**Sample:** 
  ```
  {
    "id": 2,
    "email": "test1@gmail.com",
    "created_timestamp": "2022-12-27T10:58:01.244421Z",
    "updated_timestamp": "2022-12-27T10:58:01.244421Z"
  }
  ```

### api/v1/signin/
**Allowed Methods** : POST
<br>**Access Level** :  Public
<br>**fields :** 'required':  {"email","password"} Details:User must alreay have valid email and password
<br>On successfull request,JWT token and user id will be returned.
  <br>**Sample:**
```
  {
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY3MjIyNTE5NSwiaWF0IjoxNjcyMTM4Nzk1LCJqdGkiOiJkOTBmM2I4Y2Y3NmM0YmEwOWU5ZjJhMzI5Nzk4YmQ4NSIsInVzZXJfaWQiOjJ9.1u9zUCtMIdMtUcNFl4OrL6au8UqOLPq9GJd83bkqne8",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjcyMTM5MDk1LCJpYXQiOjE2NzIxMzg3OTUsImp0aSI6ImZmMWJjMmJjZTQ0YTRlMmE4MmE2YTg4MzdkNDUzNzc0IiwidXNlcl9pZCI6Mn0.Bj7y6VV3E96vwdidE7A3goRJw46w_vSj_nbPzmX7ZQg",
    "User id": 2
    }
```

### api/v1/changePassword/
**Allowed Methods** : PUT
<br>**Access Level** : Authorized users
<br>**header :** 'required': JWT access token with prefix 'Bearer' in 'Authorization'
<br>**fields :** 'required':  {"password"} Details:Password sent in the request is updated in the user profile.
<br>On successfull request,updated timestamp is returned
<br>**Sample:**
```
    {
    "updated_timestamp": "2022-12-27T10:57:43.786018Z"
     }
```

### api/v1/todolist/
**Allowed Methods** : GET
<br>**Access Level** : Authorized users
<br>**header :** 'required': JWT access token with prefix 'Bearer' in 'Authorization'
Details:
<br>On successfull request with query "http://127.0.0.1:8000/api/v1/todolist?status=<status>", todolist items of the user with given status is returned.
<br>On successfull request without query "http://127.0.0.1:8000/api/v1/todolist/,all the todolist items of the user is returned.
<br>**Sample:**
``` 
  {
        "id": 4,
        "name": "My first Task as different user",
        "description": "Can Can",
        "status": "NotStarted",
        "userid": 2,
        "created_timestamp": "2022-12-27T12:22:27.044401Z",
        "updated_timestamp": "2022-12-27T12:22:27.488325Z"
    }
```


### api/v1/todos/
**Allowed Methods** : POST
<br>**Access Level** : Authorized users
<br>**header :** 'required': JWT access token with prefix 'Bearer' in 'Authorization'
<br>**fields :** 'required':  {"name","descriptin"}Details:Todo list is created for the user with the given user and description.
<br>On successfull request todo list is created for the user.
<br>**Sample:**
```
  {
    "detail": "created"
   }
``` 
     
 ### api/v1/todos/{id}
**Allowed Methods** : PUT,DELETE
<br>**Access Level** : Authorized users
<br>**header :** 'required': JWT access token with prefix 'Bearer' in 'Authorization'
<br>**fields :**-Required only for PUT method 'required':  {"name"} or {"descriptin"} or {"status"}Details:Todo list is updated for the user with the given changes in name or description or status.
<br>For DELETE method only header is required.
<br>On successfull request  todo list is Updated or Deleted based on the method for passed Id. Error will be thrown if the id does not belong to the authorized user.
<br>**Sample for update:**
```
  {
    "detail": "updated"
   }
```

<br>**Sample for delete:**
```
  {
    "detail": "deleted"
   }
``` 


