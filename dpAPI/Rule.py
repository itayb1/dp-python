from .const import API_PATH, rule_request_body
from .base import api_call
from copy import deepcopy
from .DPEndpoint import DPEndpoint


class Rule(DPEndpoint):
    def __init__(self, auth, base_url, domain):
        DPEndpoint.__init__(self, auth=auth, base_url=base_url, domain=domain)
        self.parent_key = "StylePolicyRule"
        self.api_path = API_PATH["style_policy_rule"]


    def create(self, name, actions, direction="request-rule", **kwargs):
        """Creates a new ``style policy rule``

            Parameters:
                name (str): The name of the style policy rule
                direction (str): The direction of the style policy rule
                actions (list): A list of strings representing the actions to be attached to the style policy rule 

            Returns:
                dict: a dict/json object of new style policy rule
        """
        request_body = deepcopy(rule_request_body)
        request_body[self.parent_key]["name"] = name
        request_body[self.parent_key]["Actions"] = [ { "value": action } for action in actions]
        request_body[self.parent_key]["Direction"] = direction
        self._append_kwargs(request_body, **kwargs)
        
        response = api_call.post(self.base_url + (self.api_path).format(domain=self.domain), auth=self.auth, data=request_body)
        return request_body[self.parent_key]





