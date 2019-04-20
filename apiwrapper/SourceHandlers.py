from .const import API_PATH, http_features, mq_exclude_headers
from .base import api_call
from .DPEndpoint import DPEndpoint
from abc import ABC, abstractmethod


class SourceHandler(ABC, DPEndpoint):
    def __init__(self, auth, base_url, domain):
        DPEndpoint.__init__(self, auth=auth, base_url=base_url, domain=domain)
        ABC().__init__()


    @abstractmethod
    def create(self):
        pass


class HTTPHandler(SourceHandler):
    def __init__(self, base_url, auth, domain):
        SourceHandler.__init__(self, base_url=base_url, auth=auth, domain=domain)
        self.parent_key = "HTTPSourceProtocolHandler"
        self.api_path = API_PATH["http_handler"]


    @staticmethod
    def __get_allowed_http_features(features):
        allowed_features = http_features.copy()
        for feature in features:
            allowed_features[feature] = "on" 
        return allowed_features


    def create(self, name, local_address, local_port, state, allowed_features=(), **kwargs):
        request_features = HTTPHandler.__get_allowed_http_features(allowed_features)
        request_body = {
            "HTTPSourceProtocolHandler": {
                "name": name,
                "mAdminState": state,
                "LocalAddress": local_address,
                "LocalPort": local_port,
                "AllowedFeatures": request_features
            }
        }
        for key,value in kwargs.items():
            request_body["HTTPSourceProtocolHandler"][key] = value

        response = api_call.post(self.base_url + self._append_domain(self.api_path), auth=self.auth, data=request_body)
        return request_body["HTTPSourceProtocolHandler"]



class MQHandler(SourceHandler):
    def __init__(self, base_url, auth, domain):
        SourceHandler.__init__(self, base_url=base_url, auth=auth, domain=domain)
        self.parent_key = "MQSourceProtocolHandler"
        self.api_path = API_PATH["mq_handler"]
    

    def create(self, name, queue_manager, get_queue, state, parse_properties="on", **kwargs):
        request_body = { 
            "MQSourceProtocolHandler": {
                "name":  name,
                "mAdminState": state,
                "QueueManager": {
                    "value": queue_manager,
                },
                "GetQueue": get_queue,
                "ParseProperties": parse_properties,    
            }
        }
        for key,value in kwargs.items():
            request_body["MQSourceProtocolHandler"][key] = value

        response = api_call.post(self.base_url + self._append_domain(self.api_path), auth=self.auth, data=request_body)
        return request_body["MQSourceProtocolHandler"]
