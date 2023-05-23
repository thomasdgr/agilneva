# Agileneva - 

This microservice, produced by **Agileneva** for **TSoft-Eng** course at HES-SO Master aims to provide users with a convenient and user-friendly way to search for and discover restaurants, as well as view ratings and reviews from other users. 

## Description of the project

Authors:
- Thomas Dagier
- Antoine Blancy
- Dorian Bernasconi
- Romain Peretti
- Thibault Michaud
- Simon Cirilli
- Kiady Arintsoa
- Anthony Chevrolet

Main functionalities:
- TODO

## Running the web service - linux / mac

The web api is in the folder `/api_rest/`. We used uvicorn and fastapi for the development. You may use an own
Python virtual environment in the `/api_rest/` folder installing the python modules from `/api_rest/requirements.txt`.

- Tools should work with python3.They were used with **python 3.7**, **python 3.8** and **python 3.9**.
- Clone the repository, create virtualenv, activate the virtual env, install required packages and test.

```sh
  python3.8 -m venv venv
  source ./venv/bin/activate
  pip install --upgrade pip
  pip3 install --trusted-host pypi.python.org -r api_rest/requirements.txt
  uvicorn api_rest.main:rootapp --reload
```

Once installed, you may launch `uvicorn api_rest.main:rootapp --reload` to launch it from the terminal. The OpenAPI specifications are available under the route `/specification` and the Swagger interface to test the API under the route `/docs`. The showcase is under the route `/showcase`.

## Running the service - docker-compose

You may also use Docker (in root folder):

### Dependencies
You should have docker-compose install.

To start this docker-compose you should pull an other image from docker hub.

```sh
docker pull nikolaik/python-nodejs
```

### Run the app

```sh
  docker-compose build
  docker-compose up
```

To quit the docker image, use `exit` or `control`+ `c`

## Testing the service

If you want to test the app, you may use the following command:

```sh
  cd api_rest
  pytest -s -p no:warnings
```
