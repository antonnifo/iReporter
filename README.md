 ## IReporter   [![Build Status](https://travis-ci.org/antonnifo/iReporter.svg?branch=patch-comment-162297565)](https://travis-ci.org/antonnifo/iReporter) [![Coverage Status](https://coveralls.io/repos/github/antonnifo/iReporter/badge.svg?branch=develop)](https://coveralls.io/github/antonnifo/iReporter?branch=develop) [![Maintainability](https://api.codeclimate.com/v1/badges/f0f65e93e402e665e3c9/maintainability)](https://codeclimate.com/github/antonnifo/iReporter/maintainability) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)   


### Tech/framework used  
> python 3.6.7 and [Flask](http://flask.pocoo.org/docs/dev/)
### PROJECT OVERVIEW

Corruption is a huge bane to Africa’s development. African countries must develop novel and localised solutions that will curb this menace, hence the birth of iReporter.
iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention.   
 

## Installation and Deployment.

### Getting Started
 > git clone https://github.com/antonnifo/iReporter.git

### Seting up databases  
create two postgres databases and change the values of the database url's in your .env file   
sudo -u postgres psql 
> postgres=# create database ireporter;   
> postgres=# create database test_ireporter;


#### create a virtual environment and activate it
> python3 - m venv env  
> source .env  
> ```.env

#### Install all the dependencies using the command
> pip install - r requirements.txt  
## `contents of .env`   
```  
source venv/bin/activate  

export FLASK_ENV="development"   
export FLASK_CONFIG="development"  
export DATABASE_URL="dbname='your-database' host='localhost' port='5432' user='your-username' password='your-password'"   
export DATABASE_URL_TEST="dbname='your-test-database' host='localhost' port='5432' user='your-username' password='your-password'"   
export SECRET_KEY="secret-key-goes-here"
```

#### How to Run the App
 ```   
source .env
> flask run   
```

#### Test the application  
Tests are to be run with pytest or py.test on the root of iReporter folder
Set FLASK_CONFIG to testing on your .env file before running tests   
```
source .env
pytest --cov=app/
```




## Endpoints to test  

| Method | Endpoint                                    | Description                                    |  
| ------ | ------------------------------------------- | ---------------------------------------------- |  
|POST    |`/api/v2/auth/signup/`                        |user signs up.                                 |  
|POST    |`/api/v2/auth/signin/`                       |user signs in here.                              |  
| POST   | `/api/v2/redflags `                         | Create a red-flag record.                      |  
| GET    | `/api/v2/redflags `                         | Fetch all red-flag records.                    |  
| GET    |` /api/v2/redflags/<int:incident_id>`            | Fetch a specific red-flag record.              |  
| PATCH  | `/api/v2/redflags/<int:incident_id>/location `  | Edit the location of a specific red-flag record.        |  
| PATCH  | `/api/v2/redflags/<int:incident_id>/comment `   | Edit the comment of a specific red-flag record.         |  
| PATCH  | `/api/v2/redflags/<int:incident_id>/status `   | Edit the status of a specific red-flag record.         |
| DELETE | `/api/v2/redflag/<int:incident_id> `           | Delete a specific red flag record.             |    
|POST    |`/api/v2/interventions`                           |create an intervention record                          |  
|GET     |`/api/v2/interventions`                           |Fetch all intervention records                     |  
|GET     |`/api/v2/intervention/<int:incident_id>`         |fetch  a specific intervention record          |  
|PATCH |`/api/v2/interventions/<int:incident_id>/comment`    |update an intervention's comment              |  
|PATCH|`/api/v2/interventions/<int:incident_id>/location`    |update an intervention's location              |  
| DELETE | `/api/v2/interventions/<int:incident_id> `           | Delete a specific intervention record.   |  
|PATCH|`/api/v2/interventions/<int:incident_id>/status`    |update an intervention's status              |  



 ### Documentation  
 [Postman Documentation](https://web.postman.co/collections/5023026-c3790353-e44a-4692-921d-6071942cbcc4?workspace=4d54ae63-9d4b-4731-82b0-90598d247bfc "My postman docs link")
 
 #### Author  
 > Anthony Mwangi
 
