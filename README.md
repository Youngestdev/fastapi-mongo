# FastAPI + MongoDB

A simple starter for building RESTful APIs with FastAPI and MongoDB. 

## Features

+ Python FastAPI backend.
+ MongoDB database.
+ Authentication
+ Deployment

## How To Use

Clone this repository and make a virtual environment in it. Install the modules listed in the `requirements.txt` file:

```console
pip3 install -r requirements.txt
```

To run the starter:

First, set your `PYTHONPATH`:

```console
export PYTHONPATH=$PWD
```

Next:

```console
python app/main.py
```

You also need to start your mongodb instance.

The starter listens on port 8000 on address [0.0.0.0](0.0.0.0). 

![FastAPI-MongoDB starter](https://res.cloudinary.com/adeshina/image/upload/v1600180509/fopab9idhrjqeqds4izk.png)

## Deploying to Vercel

> Currently, the vercel build fails when running requests to MongoDB through the async driver. The next section shows how to deploy to Heroku.

To deploy to [vercel](https://vercel.com), make sure the `vercel` CLI tool is installed and run the command in the base directory:

```console
vercel 
```

The above deploys to development, to deploy it into production, run:

```console
vercel --prod
```

Ensure you add the environment variable `MONGO_DETAILS` in vercel.

## Deploying to Heroku

To deploy to Heroku, connect your repository to the Heroku application and deploy the branch master. This template has been deployed to Heroku and you can view it here: [FastAPI Mongo](https://fastapi-mongo.herokuapp.com/)

Ensure you add the environment variable `MONGO_DETAILS` in your application's settings.

## Dockerising

To build a docker image for this boilerplate, create a duplicate `.env` file but with name `env`. Next, build an image:

```console
docker build -t fastapi-mongo .
```

The command above builds an image that can be deployed. To run the image in a container:

```console
docker run --env-file env -d --name fastapi-mongo -p 80:80 fastapi-mongo:latest
```

## Contributing ?

Fork the repo, make changes and send a PR. We'll review it together!

## TODOS

- [ ] Add a simple bash script file that runs the installation process.

- [x] Fix the `UPDATE` part of the CRUD operation

- [x] Add Authentication

- [x] Add Dockerfile

- [x] Vercel configuration file

- [x] Deploying to Heroku

- [ ] Write a concise README

- [x] Format code. I'm new to FastAPI so I'll be working towards best practices.


## License

This project is licensed under the terms of MIT license.
