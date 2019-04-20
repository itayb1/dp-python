from .const import API_PATH, MPGW_request_body, policy_attachment_request_body
from .base import api_call
from .DPEndpoint import DPEndpoint


class MPGW(DPEndpoint):
    def __init__(self, auth, base_url, domain):
        DPEndpoint.__init__(self, auth=auth, base_url=base_url, domain=domain)
        self.parent_key = "MultiProtocolGateway"
        self.api_path = API_PATH["mpgw"]


    def create(self, name, front_handlers, xml_manager, style_policy, state="enabled"):
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
        request_body = MPGW_request_body.copy()
        self.__create_mpgw_policy_attachment(name)
        request_body["MultiProtocolGateway"]["name"] = name
        request_body["MultiProtocolGateway"]["FrontProtocol"] = [ { "value": handler } for handler in front_handlers ]
        request_body["MultiProtocolGateway"]["mAdminState"] = state
        request_body["MultiProtocolGateway"]["XMLManager"] = { "value": xml_manager }
        request_body["MultiProtocolGateway"]["StylePolicy"] = { "value": style_policy } 
        request_body["MultiProtocolGateway"]["PolicyAttachments"] = { "value": name } 
        

        response = api_call.put(self.base_url + (self.api_path+"/{name}").format(domain=self.domain, name=name), auth=self.auth, data=request_body)
        return request_body["MultiProtocolGateway"]
    
    
    def __create_mpgw_policy_attachment(self, name):
        request_body = policy_attachment_request_body.copy()
        request_body["PolicyAttachments"]["name"] = name
        return api_call.put(self.base_url + (API_PATH["policy_attachments"]+"/{name}").format(domain=self.domain, name=name), auth=self.auth, data=request_body)
        

