# CRUD REST API

## Tech Stacks
- Flask
- MongoDB(compass)

# Flask Web API that simulates the behavior of an audio file server while using a MongoDB / SQL database.

# DataBase Schema Design
## Song file fields:
- ID – (mandatory, integer, unique)
- Name of the song – (mandatory, string, cannot be larger than 100 characters)
- Duration in number of seconds – (mandatory, integer, positive)
- Uploaded time – (mandatory, Datetime, cannot be in the past)

# Create API:
## The request will have the following fields:
- audioFileType – mandatory, one of the 3 audio types possible
- audioFileMetadata – mandatory, dictionary, contains the metadata for one of the three audio files (song, podcast, audiobook)

# Delete API:
- The route will be in the following format: **audioFileType>/<audioFileID**

# Update API:
- The route be in the following format: **audioFileType>/<audioFileID**
- The request body will be the same as the upload
 
# Get API:
- The route **audioFileType/audioFileID** will return the specific audio file
- The route **audioFileType** will return all the audio files of that type

## The response of these methods should be one of the following:
- Action is successful: 200 OK 
- The request is invalid: 400 bad request 
- Any error: 500 internal server error

# Installation 
## Database Setup

- Install a NoSql database **MongoDB** Compass or Shell in OS [Install Link](https://docs.mongodb.com/manual/installation/).
- Open a mongodb compass and create a database called **audioserver**.
- Create a Collection called **songs**.
- In song collection design the above defined schema. 

<img src='image results/database.png' width="490px" >

## Running Flask API
 - Make a clone on this repository 
 - Install _Flask_ and _Flask SqlAlchemy_ python libraries in the code editor
 - Run the program on your editor by using the command `python app.py` 
 - It will be run on the localhost `http://127.0.0.1:5000/` 

# Testing 
## Tools - Postman Software [Installation link](https://www.postman.com/downloads/)

## Give an API reuest in the postman application 
- Add new song `http://127.0.0.1:5000/add` **Method=POST**
- Display all songs `http://127.0.0.1:5000/songs` **Method=GET**
- Find particular song by using song id `http://127.0.0.1:5000/song/609e04802ea519b84bcc2526` **Method=GET**
- Update any song details `http://127.0.0.1:5000/update/609e04802ea519b84bcc2526` **Method=UPDATE**
- Delete any song `http://127.0.0.1:5000/delete/609e04802ea519b84bcc2526`  **Method=DELETE**

# Image Results 

## CREATE  
<img src='image results/add song.png' width="490px" >

## READ  
<img src='image results/read song.png' width="490px" >

## UPDATE  
<img src='image results/updatesong.png' width="490px" >

## DELETE 
<img src='image results/deletesong.png' width="490px" >

## DISPLAY
<img src='image results/display all.png' width="490px" >
