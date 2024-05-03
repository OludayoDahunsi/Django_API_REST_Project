## 1. Introduction
# Project Name: SAFEHR – Backend Functionality Evaluation 
### (Project focus - Endpoint Framework Migration and Functionality Enhancement)

This project is about the SAFEHR application used by the  Minnesota State University, Mankato School of Nursing Program. The SAFEHR
application is simulated electronic health records that provide students with a virtual environment to practice clinical simulation 
functionalities scenarios.

The software currently runs a deprecated version of the Sencha Torch framework and an older version of Laravel, which no longer has mainstream 
support and has reached its end of life. This makes this program unreliable and an insecure stack of technology.

### Project Purpose and scope
The purpose of the project is to evaluate the current existing backend functionality and source code artifacts. 
- Re-engineer the SAFEHR backend endpoint,
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

### If you decide to clone the repository, and run in a containerized environment. You do not need a fresh install of the Django and Django REST Framework 

### Cloning the repository Or Installing Afresh

### Cloning the repository
This step-by-step series shows you how to get a development environment running:
1. Install dependencies
  - Python 3.12.3
2. Install Container and Database client
  - Docker Container (Docker Hub)
  - Microsoft SQL Server
  - MySQL Workbench
3. Clone the repository
4. Activate the virtual environment.
    ###  Running from Git bash.
    `source venv/Script/activate`
    ###  Running from the VScode terminal
    `cd venv/Script/activate`
5. Run the server
    ###  Running the server
    `python manage.py runserver`

### Installing Afresh
Create a project folder
1. Install dependencies
  - Python 3.12.3
2. Setting up the virtual environment for the project
    `python -m venv venv`
   Activate the virtual environment
    ###  Running from Git bash.
    `source venv/Script/activate`
    ###  Running from the VScode terminal
    `cd venv/Script/activate`
3. Django Installation
    `pip install Django`
4. Installing the Django REST framework
`pip install Djangorestframework`

  ### Creating the SAFEHR project folder
      `django-admin startproject Safehr .`

5. Adding the rest framework into you settings
   
     ` INSTALLED_APPS = [
   'rest_framework', ] `
  
5. Install Container and Database clients
  - Docker Container (Docker Hub)
  - Microsoft SQL Server
  - MySQL Workbench

Navigate the manage.py directory
   - 
    
    
  - 



## 3. Usage
Explain how to use the system. This could include:

- How to make API calls (include examples with `curl` or another tool).
- What kind of responses to expect.
- How to handle errors.

```markdown
## Usage
Here are some examples of how to use the API:

### Get a list of all items
`GET /api/items/`

### Get a specific item
`GET /api/items/{id}/`
```

## 4. Running the Tests
Explain how to run the automated tests for this system.

```markdown
## Running the Tests
Explain how to run the automated tests for this system:

`python manage.py test`
```

## 5. Deployment
Add additional notes about how to deploy this on a live system.

```markdown
## Deployment
Add additional notes about how to deploy this on a live system.
```

## 6. Contributing
If you want others to contribute to the project, provide instructions on how they should do so.

```markdown
## Contributing
Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.
```

## 7. Versioning
State which versioning methodology you are using, if any.

```markdown
## Versioning
We use [SemVer](http://semver.org/) for versioning.
```

## 8. Authors
Acknowledge those who contributed to the project.

```markdown
## Authors
- Your Name - Initial work - [YourName](https://github.com/yourname)
```

## 9. License

This project is licensed and approved under supervision of Professor Flint Million, Minnesota State University Mankato after the proposal approval

## 10. Acknowledgments
- I wHat tip to anyone whose code was used
- Inspiration
- etc
```
