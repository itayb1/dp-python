from .const import API_PATH, xml_manager_request_body
from .base import api_call
from copy import deepcopy
from .DPEndpoint import DPEndpoint


class XmlManager(DPEndpoint):
    def __init__(self, auth, base_url, domain):
        DPEndpoint.__init__(self, auth=auth, base_url=base_url, domain=domain)
        self.parent_key = "XMLManager"
        self.api_path = API_PATH["xml_manager"]


    def create(self, name, user_agent="default", virtual_servers=None, **kwargs):
        """Creates a new ``XMLManager``

            Parameters:
                name (str): The name of the xml manager
                user_agent (str): The user agent to attach.
                virtual_servers (list): A list of strings with the names of the LBGs to attach. 

            Returns:
                dict: a dict/json object of xml manager.
        """
        request_body = deepcopy(xml_manager_request_body)
        request_body[self.parent_key]["name"] = name
        request_body[self.parent_key]["UserAgent"]["value"] = user_agent
        if virtual_servers:
            request_body[self.parent_key]["VirtualServers"] = [ { "value": lbg } for lbg in virtual_servers]
        self._append_kwargs(request_body, **kwargs)
        
        response = api_call.post(self.base_url + (self.api_path).format(domain=self.domain), auth=self.auth, data=request_body)
        return request_body[self.parent_key]
