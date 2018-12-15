 [![Build Status](https://travis-ci.org/antonnifo/iReporter.svg?branch=patch-comment-162297565)](https://travis-ci.org/antonnifo/iReporter) [![codecov](https://codecov.io/gh/antonnifo/iReporter/branch/patch-comment-162297565/graph/badge.svg)](https://codecov.io/gh/antonnifo/iReporter) [![Maintainability](https://api.codeclimate.com/v1/badges/f0f65e93e402e665e3c9/maintainability)](https://codeclimate.com/github/antonnifo/iReporter/maintainability)   
 ## IReporter

### Tech/framework used  
> python 3.6.7 and Flask
### PROJECT OVERVIEW

Corruption is a huge bane to Africa’s development. African countries must develop novel and localised solutions that will curb this menace, hence the birth of iReporter.
iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention.

## Installation and Deployment.

### Clone the repo
 > git clone https://github.com/antonnifo/iReporter.git

### Setup environment  
create a database called ireporter or create one to your liking and change the url in app/db_con.py  
sudo -u postgres psql.use your local user also. 
> postgres=# create database ireporter;


#### create a virtual environment and activate it
> python3 - m venv env  
> source .env  
> ```.env

#### Install all the dependencies using the command
> pip install - r Requirements.txt  
## `.env`  
> source venv/bin/activate  
>export FLASK_APP = run.py  
> FLASK_CONF = "development"  
>FLASK_DEBUG = 1  
>FLASK_ENV = "development"  


#### How to Run the App
> ```.env
> flask run

#### Test the application
> flask test  
> or  
> flask cov



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
 
                    









