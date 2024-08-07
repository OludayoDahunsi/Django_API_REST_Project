## 1. Introduction
# Project Name: SAFEHR – Backend Functionality Evaluation 
### (Project focus - Endpoint Framework Migration and Functionality Enhancement)

This project is about the SAFEHR application used by the  Minnesota State University, Mankato School of Nursing Program. The SAFEHR
application is simulated electronic health records that provide students with a virtual environment to practice clinical simulation 
functionalities scenarios.

The software currently runs a deprecated version of the Sencha Torch framework and an older version of Laravel, which no longer has mainstream 
support and has reached its end of life. This makes this program unreliable and an insecure stack of technology.

### Project Purpose and scope
The project aims to evaluate the current existing backend functionality and source code artifacts. 
- Reengineer the SAFEHR backend endpoint,
- Migrate the SAFEHR Endpoint to a new mainstream framework and
- Enhance the functionalities

This project will be rebuilt to utilize the following framework:
- Django and
- Django REST API Framework

The project will be containerized
- Docker Container

The endpoints will be tested
- Postman


## 2. Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing. The follow prerequisites

### Prerequisites software
- Python 3.12.3
- Django
- Django REST Framework
- Microsoft SQL Server
- MySQL Workbench
- Docker Container
- Git Bash
- Postman

### If you clone the repository, run it in a containerized environment. You do not need a fresh install of the Django and Django REST Framework. (One way to access the project is by cloning the repository Or Setting up a fresh environment.)

### Cloning the repository
This step-by-step series shows you how to get a development environment running:
#### Install dependencies
  - Python 3.12.3
#### Install Container and Database client
  - Docker Container (Docker Hub)
  - Microsoft SQL Server
  - MySQL Workbench
#### Clone the repository for the GitHub
#### Activate the virtual environment.
    ###  Running from Git bash.
    ` source venv/Script/activate `
    ###  Running from the VScode terminal
    ` cd venv/Script/activate `
#### Run the server
    ` python manage.py runserver `

### DJANGO fresh Installations
- Create a project folder and Install dependencies
  - Python 3.12.3 is installed for this project
- Setting up the virtual environment for the project
    `python -m venv venv`

- Activate the virtual environment
    ####  Running from Git bash.
    `source venv/Script/activate`
    ####  Running from the VScode terminal
    `cd venv/Script/activate`
- Django Installation
    `pip install Django`
- Installing the Django REST framework
    `pip install Djangorestframework`

- Creating the SAFEHR project folder
   `django-admin startproject Safehr .`

- Adding the rest_framework into your settings
    ```
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    ]

- Migrate all the Django programs installed
   `  python manage.py migrate  `
  
- Running the Server from Git Bash or terminal, these are the command in order of arrangement
   `wintpty python manage.py runserver` OR
   `python manage.py runserver`
    
- Install Container and Database clients
  - Docker Container (Docker Hub)
  - Microsoft SQL Server
  - MySQL Workbench
   
 ### Creating Django App with startapp 
     `  python manage.py startapp backendapp  ` 

 
 ### Adding the backendapp into your settings
    ```
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'backendapp',
    ]


 ### Configure the url.py in safehr directory 
 ```  url.py in the safehr

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('backendapp.urls'))
  ```

### Create a URL in the backendapp  to display API endpoints ` urls.py `
 ```
 
from django.urls import path, include
from . import views

urlpatterns = [

    path ('', include(router.urls))
    
]
  ```

### Accessing the created admin at 127.0.0.1:8000/admin
   - username: admin
   - password: safehrapi


## Setting up the database 
   - For the purpose of the project, we have created the SAFEHR2 Database for both MySQL and MSSQL
   - Install pyodbc and pysql drivers (check the documentation headings provided below)
    
  #### MSSQL Database
  #### Documentation: https://pypi.org/project/mssql-django/
  ```
  DATABASES = {
        'default': {
            'ENGINE': 'mssql',
            'NAME': 'SAFEHR',
            'USER': 'sa',
            'PASSWORD': 'DDDDDDDDDDD',
            'HOST': 'campus-quest.com',
            'PORT': '20011',

            'OPTIONS': {
                'driver': 'ODBC Driver 17 for SQL Server',
            },
        },
    }
  ```

#### MySQL Database
#### Documentation: https://pypi.org/project/mysqlclient/
  ```
  DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'Safehr2',
            'USER': 'root',
            'PASSWORD': 'DDDDDDDDDDD!',
            'HOST': 'campus-quest.com',
            'PORT': '20010',

            'OPTIONS': {
                'sql_mode': 'STRICT_TRANS_TABLES',
            }
        },
    }
  ```
  
## Other necessary configuration



## 3. Building the Endpoints using Django REST Framework:

```
This process of building the endpoints involves creating the
  - Models: models.py - used to create the class and the model to access or call the data from the databases
  - Views: view.py  This handles the request and response for webpage application
  - Serializers: These take the data from the databases and translate TO and FROM JSON to allow the PI to send data around the internet  
  - Setting up models: models.py This is used to define the data models for the app
  - Router in the URL(Url.py located in the API app i.e backendapp) - 
  - Admin -admin.py This is where models are registered
      #### and permissions. You can also use generics, mixins, view sets, and routers to simplify your API code

```

## 4. Make a Migration
After each model is set, make a migration and migrate the models to the Databases.

```
## Make Migration
    - python manage.py makemigrations
## Migrate
    - python manage.py migrate
```

      
## 5. Usage

```
This explains how to use the system. This  includes:

- How to make API calls ( with `POSTMAN`).
- Output responses are expected from each endpoint.
- The response depends on the particular endpoint you called
```


## Usage
Here are some examples of how to use the API:

### Get a list of all patient
``` 
    `GET /api/patient/`

    "Persons": "http://127.0.0.1:8000/Persons/",
    "Person_Address": "http://127.0.0.1:8000/Person_Address/",
    "Person_Organization": "http://127.0.0.1:8000/Person_Organization/",
    "Person_Phone": "http://127.0.0.1:8000/Person_Phone/",
    "Person_Historical_Diagnostic": "http://127.0.0.1:8000/Person_Historical_Diagnostic/",
    "Address": "http://127.0.0.1:8000/Address/",
    "Diagnostic": "http://127.0.0.1:8000/Diagnostic/",
    "Organization_Address": "http://127.0.0.1:8000/Organization_Address/",
    "Clinic": "http://127.0.0.1:8000/Clinic/"

### Get a specific patient detail
`GET /api/patient/{id}/`

"Persons": "http://127.0.0.1:8000/Persons/1/"

```



## 6. Running the Tests
Running the automated tests for this project.
```
## Copy the endpoint URL into the POSTMAN

` http://127.0.0.1:8000/Persons/1/ `

` Every data access via DJANGO URL will be populated in POSTMAN.`

## Run a GET, POST, DELETE from the POSTMAN
` You will be able to GET, POST, DELETE.`

```

```
## Handling Errors
- How to handle errors.
If you encounter an error, check the errors
  - VS code Terminal or the Git Bash Terminal
  - Locate the line where the error occurred
  - The clue to error handling is to take time to read the error output on the terminal

```

## 7. Versioning

```
## Versioning
We use GitHub (https://github.com/) for versioning.
```

## 8. Authors
```
## Authors
- ​​Oludayo A Dahunsi   - https://github.com/OludayoDahunsi
- Joy Chepkirui - https://github.com/JoyChepkirui1
- Manojkumar Rajanna - https://github.com/Manoj9901
- ​Victor Chirchir 
- Solomon Aryee

```

## 9. Project Approval 
```
This project is approved course code CIS 680 and implemented under the supervision of Professor Flint Million, Minnesota State University Mankato.
```

## 10. Acknowledgments
```
- I appreciate everyone's contributions to this project. Your contributions have been invaluable, and your coding skills are truly impressive. 
- Thank you for your hard work and dedication.
```
