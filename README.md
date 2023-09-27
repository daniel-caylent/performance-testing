
This simple library is an API performance analytics tool. It's sole purpose is to collect execution times for specific test cases, which are defined in the code.

# Setup

python3 -m venv .venv
source ./.venv/bin/activate
pip3 install -r requirements.txt

# Define your test cases

Tests are stored in the variable `tests = []`
The base URL for your tests is saved in `BASE_URL = ""`

Test case definitions use the following schema:

```

{
    "name": "fastapi-cold-start-POST-failure", # the name of the test, used to generate the results file
    "sleep": 360, # how many seconds to wait between iterations of this test
    "url": "/fastapi", # what URL to append to the BASE_URL to complete the request
    "method": "POST", # what time of request (only GET and POST are supported at the moment)
    "expected_code": 201, # The response code we're expecting
    "data": {
        "name": "test", # this data will be passed with the request. If the METHOD is a POST
        "number": "a"   # it will be send in the request body; for a GET they will be passed as URL parameters
    },
    "repetitions": 50 # how many times this test should be repeated
}

```