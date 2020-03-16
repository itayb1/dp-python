from .const import API_PATH, MPGW_request_body, policy_attachment_request_body
from .base import api_call
from copy import deepcopy
from .DPEndpoint import DPEndpoint


class MPGW(DPEndpoint):
    def __init__(self, auth, base_url, domain):
        DPEndpoint.__init__(self, auth=auth, base_url=base_url, domain=domain)
        self.parent_key = "MultiProtocolGateway"
        self.api_path = API_PATH["mpgw"]


    def create(self, name, front_handlers, xml_manager, style_policy, state="enabled", **kwargs):
        """Creates a new ``Multi Protocol Gateway``

        Parameters:
            name (str): The name of the mpgw
            front_handlers (list): A list of strings representing front handlers to be attached to the mpgw
            xml_manager (str): The name of the xml manager to be attached to the mpgw
            style_policy (str):  The name of the style policy to be attached to the mpgw
            state (str): The state of the mpgw (default is enabled)

        Returns:
            dict: a dict/json object of the new mpgw
        """
        request_body = deepcopy(MPGW_request_body)
        self.__create_mpgw_policy_attachment(name)
        request_body[self.parent_key]["name"] = name
        request_body[self.parent_key]["FrontProtocol"] = [ { "value": handler } for handler in front_handlers ]
        request_body[self.parent_key]["mAdminState"] = state
        request_body[self.parent_key]["XMLManager"] = { "value": xml_manager }
        request_body[self.parent_key]["StylePolicy"] = { "value": style_policy } 
        request_body[self.parent_key]["PolicyAttachments"] = { "value": name } 
        self._append_kwargs(request_body, **kwargs)

        response = api_call.post(self.base_url + (self.api_path).format(domain=self.domain), auth=self.auth, data=request_body)
        return request_body[self.parent_key]
    
    
    def __create_mpgw_policy_attachment(self, name):
        request_body = deepcopy(policy_attachment_request_body)
        request_body["PolicyAttachments"]["name"] = name
        return api_call.post(self.base_url + (API_PATH["policy_attachments"]).format(domain=self.domain), auth=self.auth, data=request_body)
        

