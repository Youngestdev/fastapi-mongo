# FastAPI + MongoDB

A simple starter for building RESTful APIs with FastAPI and MongoDB. 

## Features

+ Python FastAPI backend.
+ MongoDB database.
+ Authentication [Coming soon]
+ Deployment [coming soon]

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

![FastAPI-MongoDB starter](https://res.cloudinary.com/adeshina/image/upload/v1599469492/gwzjqryzfvufftyypldo.png)

## Deploying to Vercel

To deploy to [vercel](https://vercel.com), make sure the `vercel` CLI tool is installed and run the command in the base directory:

```console
vercel 
```

The above deploys to development, to deploy it into production, run:

```console
vercel --prod
```

After the installations, add your `MONGO_DETAILS` environment value in Vercel.

## Dockerising [TODO]

I'll write a short blog post on this or maybe a mini section here. It's a todo!

## Contributing ?

Fork the repo, make changes and send a PR. We'll review it together!

## TODOS

[ ] Add a simple bash script file that runs the installation process.

[x] Fix the `UPDATE` part of the CRUD operation

[ ] Add Authentication

[ ] Add Dockerfile

[x] Vercel configuration file

[ ] Write a concise README

[x] Format code. I'm new to FastAPI so I'll be working towards best practices.


## License

This project is licensed under the terms of MIT license.
