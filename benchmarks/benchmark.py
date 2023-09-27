import time

import requests


BASE_URL = "https://mv9f04rfy9.execute-api.us-east-1.amazonaws.com/v1"
FILE_SUFFIX = "-benchmarks.txt"

tests = [
    {
        "name": "custom-warm-start-GET-success",
        "sleep": .1,
        "url": "/custom",
        "method": "GET",
        "expected_code": 200,
        "data": {
            "search": "test"
        },
        "repetitions": 51
    },
    {
        "name": "custom-warm-start-GET-failure",
        "sleep": .1,
        "url": "/custom",
        "method": "GET",
        "expected_code": 400,
        "data": {
            "search1": "test"
        },
        "repetitions": 51
    },
    {
        "name": "custom-warm-start-POST-success",
        "sleep": .1,
        "url": "/custom",
        "method": "POST",
        "expected_code": 201,
        "data": {
            "name": "test",
            "number": 1
        },
        "repetitions": 51
    },
    {
        "name": "custom-warm-start-POST-failure",
        "sleep": .1,
        "url": "/custom",
        "method": "POST",
        "expected_code": 400,
        "data": {
            "name": "test",
            "number": "a"
        },
        "repetitions": 51
    },
    {
        "name": "fastapi-warm-start-GET-success",
        "sleep": .1,
        "url": "/fastapi",
        "method": "GET",
        "expected_code": 200,
        "data": {
            "search": "test",
        },
        "repetitions": 51
    },
    {
        "name": "fastapi-warm-start-POST-success",
        "sleep": .1,
        "url": "/fastapi",
        "method": "POST",
        "expected_code": 201,
        "data": {
            "name": "test",
            "number": 1
        },
        "repetitions": 51
    },
    {
        "name": "fastapi-warm-start-POST-failure",
        "sleep": .1,
        "url": "/fastapi",
        "method": "POST",
        "expected_code": 422,
        "data": {
            "name": "test",
            "number": "a"
        },
        "repetitions": 51
    },
    {
        "name": "custom-cold-start-POST-failure",
        "sleep": 360,
        "url": "/custom",
        "method": "POST",
        "expected_code": 400,
        "data": {
            "name": "test",
            "number": "a"
        },
        "repetitions": 51
    },
    {
        "name": "custom-cold-start-POST-success",
        "sleep": 360,
        "url": "/custom",
        "method": "POST",
        "expected_code": 201,
        "data": {
            "name": "test",
            "number": 1
        },
        "repetitions": 51
    },
    {
        "name": "fastapi-cold-start-GET-success",
        "sleep": 360,
        "url": "/fastapi",
        "method": "GET",
        "expected_code": 200,
        "data": {
            "search": "test",
        },
        "repetitions": 51
    },
    {
        "name": "custom-cold-start-GET-success",
        "sleep": 360,
        "url": "/custom",
        "method": "GET",
        "expected_code": 200,
        "data": {
            "search": "test"
        },
        "repetitions": 50
    },
    {
        "name": "custom-cold-start-GET-failure",
        "sleep": 360,
        "url": "/custom",
        "method": "GET",
        "expected_code": 400,
        "data": {
            "search1": "test"
        },
        "repetitions": 51
    },
    {
        "name": "fastapi-cold-start-GET-failure",
        "sleep": 360,
        "url": "/fastapi",
        "method": "GET",
        "expected_code": 422,
        "data": {
            "search1": "test",
        },
        "repetitions": 51
    },
    {
        "name": "fastapi-warm-start-GET-failure",
        "sleep": .1,
        "url": "/fastapi",
        "method": "GET",
        "expected_code": 422,
        "data": {
            "search1": "test",
        },
        "repetitions": 51
    },
    {
        "name": "fastapi-cold-start-POST-success",
        "sleep": 360,
        "url": "/fastapi",
        "method": "POST",
        "expected_code": 201,
        "data": {
            "name": "test",
            "number": 1
        },
        "repetitions": 51
    },
    {
        "name": "fastapi-cold-start-POST-failure",
        "sleep": 360,
        "url": "/fastapi",
        "method": "POST",
        "expected_code": 422,
        "data": {
            "name": "test",
            "number": "a"
        },
        "repetitions": 51
    },
]

def write_output(name, data):
    data_str = "\n".join(data)
    with open(f"{name}-{FILE_SUFFIX}", "w") as file_:
        file_.write(data_str)

def send_post_request(test_case):
    return requests.post(
        f"{BASE_URL}{test_case['url']}", json=test_case["data"]
    )

def send_get_request(test_case):
    url = f"{BASE_URL}{test_case['url']}"
    return requests.get(url, test_case["data"])

def execute_test(test_case):
    if test_case["method"] == "GET":
        return send_get_request(test_case)
    elif test_case["method"] == "POST":
        return send_post_request(test_case)

def main():
    for test in tests:
        data = []
        print(test["name"])
        for i in range(test["repetitions"]):
            time.sleep(test["sleep"])

            t_start = time.time()
            result = execute_test(test)
            t_finish = time.time()

            if result.status_code != test["expected_code"]:
                raise Exception("REQUEST FAILED for test: ", test, f"\nGot status code: {result.status_code}")

            time_result = int((t_finish-t_start) * 1000)
            data.append(str(time_result))
            print(time_result)

        write_output(test["name"], data)
        

if __name__ == "__main__":
    main()




