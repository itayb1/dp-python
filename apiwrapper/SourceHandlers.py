from .const import API_PATH, http_features, mq_exclude_headers, mq_source_handler_request_body, http_source_handler_request_body
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


    def create(self, name, local_address, local_port, state, allowed_features, **kwargs):
        """Creates a new ``HTTP Source Protocol Handler``

        Parameters:
            name (str): The name of http handler
            local_address (str): alias or ip address 
            local_port (int): Port number to listen on
            state (str):  The state of the new handler - "enabled" / "disabled"
            allowed_features (list/tuple/set): A list/tuple/set of strings representing the allowed http features

        Returns:
            dict: a dict/json object of the new http source protocol handler
        """
        request_features = HTTPHandler.__get_allowed_http_features(allowed_features)
        request_body = http_source_handler_request_body.copy()
        request_body[self.parent_key]["name"] = name
        request_body[self.parent_key]["mAdminState"] = state
        request_body[self.parent_key]["LocalAddress"] = local_address
        request_body[self.parent_key]["LocalPort"] = local_port
        request_body[self.parent_key]["AllowedFeatures"] = request_features
        self._append_kwargs(request_body, **kwargs)

        response = api_call.post(self.base_url + self._append_domain(self.api_path), auth=self.auth, data=request_body)
        return request_body[self.parent_key]



class MQHandler(SourceHandler):
    def __init__(self, base_url, auth, domain):
        SourceHandler.__init__(self, base_url=base_url, auth=auth, domain=domain)
        self.parent_key = "MQSourceProtocolHandler"
        self.api_path = API_PATH["mq_handler"]
    

    def create(self, name, queue_manager, get_queue, state, parse_properties="on", **kwargs):
        """Creates a new ``MQ Source Protocol Handler``

        Parameters:
            name (str): The name of http handler
            queue_manager (str): Queue manager name 
            get_queue (int): Get queue name
            state (str):  The state of the new handler - "enabled" / "disabled"
            parse_properties (str):  "on" / "off" (default is "on")

        Returns:
            dict: a dict/json object of the new mq source protocol handler
        """
        request_body = mq_source_handler_request_body.copy()
        body = request_body[self.parent_key]
        body["name"] = name
        body["mAdminState"] = state
        body["QueueManager"]["value"] = queue_manager
        body["GetQueue"] = get_queue
        body["ParseProperties"] = parse_properties
        self._append_kwargs(request_body, **kwargs)

        response = api_call.post(self.base_url + self._append_domain(self.api_path), auth=self.auth, data=request_body)
        return request_body[self.parent_key]
