## IReporter [![Build Status](https://travis-ci.org/antonnifo/iReporter.svg?branch=patch-comment-162297565)](https://travis-ci.org/antonnifo/iReporter) [![codecov](https://codecov.io/gh/antonnifo/iReporter/branch/patch-comment-162297565/graph/badge.svg)](https://codecov.io/gh/antonnifo/iReporter) [![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/antonnifo/iReporter)

### Tech/framework used  
> python 3.6.7 and Flask
### PROJECT OVERVIEW

Corruption is a huge bane to Africa’s development. African countries must develop novel and localised solutions that will curb this menace, hence the birth of iReporter.
iReporter enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention.

### MAIN FEATURES

- Users can create an account and log in.
- Users can create a red-flag record (An incident linked to corruption).
- Users can create intervention record (a call for a government agency to intervene e.g repair bad road sections, collapsed bridges, flooding e.t.c).
- Users can edit their red-flag or intervention records.
- Users can delete their red-flag or intervention records.
- Users can add geolocation (Lat Long Coordinates) to their red-flag or intervention records.
- Users can change the geolocation (Lat Long Coordinates) attached to their red-flag or intervention records.
- Admin can change the status of a record to either under investigation, rejected (in the event of a false claim) or resolved (in the event that the claim has been investigated and resolved).
- Users can add images to their red-flag or intervention records, to support their claims.
- Users can add videos to their red-flag or intervention records, to support their claims.
- The application should display a Google Map with Marker showing the red-flag or intervention location.
- The user gets real-time email notification when Admin changes the status of their record.
- The user gets real-time SMS notification when Admin changes the status of their record.

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
| POST   | /api/v1/red-flags                           | Create a red-flag record.                      |  
| GET    | /api/v1/red-flags                           | Fetch all red-flag records.                    |  
| GET    | /api/v1/red-flags/<red-flag-id>             | Fetch a specific red-flag record.              |  
| PATCH  | /api/v1/red-flags/<red-flag-id>/location    | Edit the location of a specific record.        |  
| PATCH  | /api/v1/red-flags/<red-flag-id>/comment     | Edit the comment of a specific record.         |  
| DELETE | /api/v1/red-flags/<red-flag-id>             | Delete a specific red flag record.             |  
| PUT    | /api/v1/red-flags/<red-flag-id>             | Edit the whole red-flag record at once.        |  
 
 #### Author  
 > Anthony Mwangi
 
                    









