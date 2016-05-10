import requests
import time
import json
import random
import config

payload = {
        "operation": "create",
        "tableName": "evts-at-rest-python",
        "payload": {
            "Item": {
                "name": "FTW",
                "count": "1"
                }
            }
        }
headers = {'content-type': 'application/json'}

endpoint_node = config.ENDPOINT_BASE + "/lambda-at-rest-node"
endpoint_python = config.ENDPOINT_BASE + "/lambda-at-rest-python"
endpoint_java = config.ENDPOINT_BASE + "/lambda-at-rest-java"

def run_post(endpoint, payload):
    r = requests.post(endpoint, data=json.dumps(payload), headers=headers)
    print(r.status_code, r.reason)

while True:
    run_post(endpoint_node, payload)
    time.sleep(random.uniform(0.1, 5))
    run_post(endpoint_python, payload)
    time.sleep(random.uniform(0.1, 5))
    run_post(endpoint_java, payload)
    #time.sleep(random.uniform(90, 300))
    print("xxx")
