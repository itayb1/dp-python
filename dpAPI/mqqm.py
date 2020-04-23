from .const import API_PATH
from .base import api_call
from copy import deepcopy
from .DPEndpoint import DPEndpoint


class MQQM(DPEndpoint):
    def __init__(self, auth, base_url, domain):
        DPEndpoint.__init__(self, auth=auth, base_url=base_url, domain=domain)
        self.parent_key = "MQQM"
        self.api_path = API_PATH["mqqm"]


    def create(self, name, actions, direction="request-rule", **kwargs):
        pass




