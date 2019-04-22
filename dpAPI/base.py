import requests
import json
from .exceptions import ApiError

class api_call():
    

    @staticmethod
    def get(url, auth):
        r = requests.get(url, auth=auth, verify=False)
        response = r.json()
        if r.status_code >= 400 and r.status_code < 600 and r.status_code != 409:
            raise ApiError((" ").join(response["error"]).lower(), r.status_code)
        return response
    

    @staticmethod
    def post(url, data, auth):
        r = requests.post(url, auth=auth, data=json.dumps(data), verify=False)
        response = r.json()
        if r.status_code >= 400 and r.status_code < 600 and r.status_code != 409:
            raise ApiError((" ").join(response["error"]).lower(), r.status_code)
        return response
    
    
    @staticmethod
    def put(url, data, auth):
        r = requests.put(url, auth=auth, data=json.dumps(data), verify=False)
        response = r.json()
        if r.status_code >= 400 and r.status_code < 600 and r.status_code != 409:
            raise ApiError((" ").join(response["error"]).lower(), r.status_code)
        return response




