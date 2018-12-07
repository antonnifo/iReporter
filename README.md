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

#### create a virtual environment and activate it asap
> python3 - m venv env  
> source .env  
> ```.env

#### Install all the dependencies using the command
> pip install - r Requirements.txt

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
| POST   | `/api/v1/red-flags`                         | Create a red-flag record.                      |  
| GET    | `/api/v1/red-flags`                         | Fetch all red-flag records.                    |  
| GET    |` /api/v1/red-flags/<int:user_id>`           | Fetch a specific red-flag record.              |  
| PATCH  | `/api/v1/red-flags/<int:user_id>/location`  | Edit the location of a specific record.        |  
| PATCH  | `/api/v1/red-flags/<int:user_id>/comment`   | Edit the comment of a specific record.         |  
| DELETE | `/api/v1/red-flags/<int:user_id>`           | Delete a specific red flag record.             |  
| PUT    | `/api/v1/red-flags/<int:user_id>`           | Edit the whole red-flag record at once.        |  

 ###Documentation  
 [Postman Documentation](https://web.postman.co/collections/5023026-24407cd8-761e-4990-b552-8b76479420ab?workspace=4d54ae63-9d4b-4731-82b0-90598d247bfc#d43467be-dda1-426d-a15e-6023deb92546 "My postman docs link")
 
 #### Author  
 > Anthony Mwangi
 
                    









