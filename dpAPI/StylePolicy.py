from .const import API_PATH, style_policy_request_body
from .base import api_call
from copy import deepcopy
from .DPEndpoint import DPEndpoint


class StylePolicy(DPEndpoint):
    def __init__(self, auth, base_url, domain):
        DPEndpoint.__init__(self, auth=auth, base_url=base_url, domain=domain)
        self.__generate_policy_map = lambda match, rule: { "Match": { "value": match }, "Rule": { "value": rule } }
        self.parent_key = "StylePolicy"
        self.api_path = API_PATH["style_policy"]


    def create(self, name, policy_maps, mpgw=None, **kwargs):
        """Creates a new ``Style Policy``

        Parameters:
            name (str): The name of the style policy
            policy_maps (list): A list of tuples where each tuple contains a match action name and the appropriate rule name respectively
            mpgw (str): The name of the Multi Protocol Gateway which the style policy would be attached to
        
        Examples:
            policy map tuple - ("test_match_action", "test_rule_name")

        Returns:
            dict: a dict/json object of new style policy
        """
        request_body = deepcopy(style_policy_request_body)
        if mpgw != None:
            name = mpgw + "_policy"
        request_body[self.parent_key]["name"] = name
        request_body[self.parent_key]["PolicyMaps"] = [self.__generate_policy_map(policy_map[0], policy_map[1]) for policy_map in policy_maps]
        self._append_kwargs(request_body, **kwargs)
        response = api_call.post(self.base_url + (self.api_path).format(domain=self.domain), auth=self.auth, data=request_body)

        return request_body[self.parent_key]


    def get_rules_names(self, name):
        """Gets the names of the rules associated with the given style policy``

        Parameters:
            name (str): The name of the style policy

        Returns:
            list: a list with the names of the rules associated with the given style policy
        """
        rules = []
        resp_style_policy = self.get(name)
        policy_maps = resp_style_policy["PolicyMaps"]         
        if isinstance(policy_maps, list):
            for policy_map in policy_maps:
                rules.append(policy_map["Rule"]["value"])
        else:
            rules.append(policy_maps["Rule"]["value"])
        
        return rules
