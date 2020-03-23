from .const import API_PATH, load_balancer_group_standard, load_balancer_group_tcpconnection, load_balancer_group_member
from .base import api_call
from copy import deepcopy
from .DPEndpoint import DPEndpoint


class LoadBalanacerGroup(DPEndpoint):
    def __init__(self, auth, base_url, domain):
        DPEndpoint.__init__(self, auth=auth, base_url=base_url, domain=domain)
        self.parent_key = "LoadBalancerGroup"
        self.api_path = API_PATH["load_balancer_group"]


    def create(self, name, algorithm, members, healthcheck_type, healthcheck_port, healthcheck_uri=None, healthcheck_method=None, **kwargs):
        """Creates a new ``Load Balancer Group``

            Parameters:
                name (str): The name of the load balancer group
                algorithm (str): The algorithm to use to load balance.
                members (list): List of members to create. Exmaple to memeber creation request is below.
                healthcheck_type (str): TCPConnection or Standard.
                healthcheck_port (int): port to use for healthcheck calls.
                healthcheck_uri (str): uri to use for healthcheck calls.
                healthcheck_method (str): healthcheck method to use.
            
            Exmaples: 
                ``Member``

                    {
                            "Server": "127.0.0.1",
                            "Weight": 1,
                            "MappedPort": 9000,
                            "Activity": "",
                            "HealthPort": "",
                            "LBMemberState": "enabled"
                    }

            Returns:
                dict: a dict/json object of xml manager.
        """
        request_body = None
        if healthcheck_type == "TCPConnection": 
            request_body = deepcopy(load_balancer_group_tcpconnection)
        elif healthcheck_type == "Standard":
            request_body = deepcopy(load_balancer_group_standard)
            self.__create_standard_health_lbg(request_body, healthcheck_uri, healthcheck_method)
        else:
            return False

        request_body[self.parent_key]["name"] = name
        request_body[self.parent_key]["Algorithm"] = algorithm
        request_body[self.parent_key]["LBGroupChecks"]["SSL"] = healthcheck_type
        request_body[self.parent_key]["LBGroupChecks"]["Port"] =  healthcheck_port
        request_body[self.parent_key]["LBGroupMembers"] = members
        self._append_kwargs(request_body, **kwargs)
        
        response = api_call.post(self.base_url + (self.api_path).format(domain=self.domain), auth=self.auth, data=request_body)
        return request_body[self.parent_key]


    def __create_standard_health_lbg(self, request_body, healthcheck_uri, healthcheck_method):
        request_body[self.parent_key]["LBGroupChecks"]["URI"] =  healthcheck_uri if healthcheck_uri else request_body[self.parent_key]["LBGroupChecks"]["URI"] 
        request_body[self.parent_key]["LBGroupChecks"]["GatewayScriptReqMethod"] =  healthcheck_method if healthcheck_method else request_body[self.parent_key]["LBGroupChecks"]["GatewayScriptReqMethod"] 

