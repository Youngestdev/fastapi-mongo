# FastAPI and MongoDB Boilerplate

A simple starter for building RESTful APIs with FastAPI and MongoDB. 

## Features

+ Python FastAPI backend.
+ MongoDB database.
+ Authentication
+ Deployment

## Using the applicaiton

To use the application, follow the outlined steps:

1. Clone this repository and create a virtual environment in it:

```console
$ python3 -m venv venv
```

2. Install the modules listed in the `requirements.txt` file:

```console
(venv)$ pip3 install -r requirements.txt
```

3. Start the application:

```console
python main.py
```

You also need to start your mongodb instance.

The starter listens on port 8000 on address [0.0.0.0](0.0.0.0:8080). 

![FastAPI-MongoDB starter](https://res.cloudinary.com/adeshina/image/upload/v1600180509/fopab9idhrjqeqds4izk.png)

## Deployment

This application can be deployed on any PaaS such as [Heroku](https://heroku.com) or [Okteto](https://okteto) and any other cloud service provider.


## Contributing ?

Fork the repo, make changes and send a PR. We'll review it together!

## License

This project is licensed under the terms of MIT license.