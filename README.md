# GitHubAPI
<!-- ABOUT THE PROJECT -->
## About The Project
The GitHub repository viewer is an application designed to provide a fast overview of essential details about repositories and users. It acquires repository information from GitHub's REST API endpoints, utilizing the HTTP protocol for both delivering data to users and fetching data from GitHub.

<!-- TECHNOLOGIES USED -->
## Technologies used
* Python
* RestAPI, FastAPI
* Docker
* Uvicorn

<!-- PREREQUISITES -->
## Prerequisites
* Python
* Pip
* Uvicorn
* Docker *(optional)*

<!-- INSTALLATION AND USAGE -->
## Installation
Application can be set up in two ways. 

### First way:
* clone repository

  `git clone https://github.com/Turtlesome/GithubAPI.git`

* cd into project directory

* To install all needed libraries use this command:

  `pip install -r requirements.txt`

* run project using

  `uvicorn main:app --reload`

### Second way:
* Approach revolves around using docker to set up docker container and start app inside it. Docker image can be downloaded directly from DockerHub with using:

  `docker run -e GITHUB_TOKEN="Your_Github_Token" -p 8000:8000 turtlytortoise/githubapi`

* or either built locally with Dockerfile that can be found in the main folder of the project:

  `docker build -t githubapi .`

* and then:

  `docker run -e GITHUB_TOKEN="Your_Github_Token" -p 8000:8000 githubapi`

### Third way:
* Third approach is just starting the app in the IDE after cloning the repository.
To install all needed libraries use this command:

  `pip install -r requirements.txt`


<!-- INSTALLATION AND USAGE -->
## Functionalities
In current state of the app, all endpoints are accessible via HTTP requests on localhost:8000.

Application has four basic functionalities. 
1. It provides with list of all user's public repositories with options for sorting them by:
   
   a) name alphabetically (default behaviour)

   b) stars (from lowest to highest number or reverse) --> add after '?' sort_by=stars or sort_by=starsR, for example `http://localhost:8000/users/torvalds/repos?sort_by=stars`

   c) date created (from latest) --> add after '?' sort_by=created

   d) date updated (from latest) --> add after '?' sort_by=updated

All four endpoints are shown below:

* GET all public repositories owned by a user and save them to json file

  `http://localhost:8000/users/{user_id}/repos`

* GET information about particular user by their name

  `http://localhost:8000/users/{user_id}`

* GET information about current pull requests

  `http://localhost:8000/{user_id}/{repo_id}/pulls`
  
* GET list of files in particular repositorium save them to json file

  `http://localhost:8000/{user_id}/{repo_id}/files`

## Future development

  There is of course room for extending current functionalities getting more or specific information from github. Moreover, there is need for providing some information into logs.
