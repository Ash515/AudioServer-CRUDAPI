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

# Testing 
## Tools - Postman Software

## CREATE  
<img src='image results/add song.png' width="500px" height="400px">