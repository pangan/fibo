# Fibonacci Service
This tiny service returns Fibonacci item __n__ and __n__ will be increased by __1__ after each call. 

## Settings
`fib/settings.py` is used for application settings :

```
# it starts to return from the first Fibonacci item after reaching this limit.
MAXIMUM_FIB_LENGTH = 100
```

## How to run it

### Docker

Just run the below command:

   `docker-compose up`

It will create the image and runs the services in docker.
You can access the service at the following url:

`http://localhost:8080` 

### Running on your machine

* Make a python 3.7 virtual environment:

    `virtualenv .venv`

* Active the virtual environment:

    `source .venv/bin/activate`

*  Install the requirements:

    `pip install -r requirements.txt`

* Run the application:

    * `gunicorn -b0.0.0.0:8080 --reload -w1 fib:api`

* You can access the application at the following url:

    `http://localhost:8080`
    
## Tests

* Below command will run all the tests:

	* ```make test ```
	
* Unit tests:

	* ```make unittess```
	
* PEP8 test:

	* ```make flake```

* Test formatting:

	* ```make testformatting```

* Test typing:

	* ```make testtyping```