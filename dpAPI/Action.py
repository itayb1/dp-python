from .const import API_PATH, validate_action_request_body, transform_action_request_body, result_action_request_body, gateway_script_action_request_body, slm_action_request_body
from .base import api_call
import uuid
from copy import deepcopy
from .DPEndpoint import DPEndpoint
from .slm import SLM


class Action(DPEndpoint):
    def __init__(self, auth, base_url, domain):
        DPEndpoint.__init__(self, auth=auth, base_url=base_url, domain=domain)
        self.parent_key = "StylePolicyAction"
        self.api_path = API_PATH["style_policy_action"]
        self.schema_types = {"json": "JSONSchemaURL", "xml": "SchemaURL"}


    def create(self):
        pass
    

    def create_validate_action(self, schema_url, schema_type, name=None, rule_name=None, uid=None, **kwargs):
        """Creates a new ``validate action``

        Parameters:
            name (str): The name of the action
            schema_url (str): The schema location on DataPower
            schema_type (str): The schema type
            rule_name (str): The name of the rule which the new validate action would be attached to

        Returns:
            dict: a dict/json object of new validate action
        """
        request_body = deepcopy(validate_action_request_body)
        request_body[self.parent_key]["name"] = self.create_name_by_convention(rule_name, "validate", uid) if (rule_name != None and name == None) else name
        name = request_body[self.parent_key]["name"]
        schema_request_key = self.schema_types.get(schema_type.lower())
        if schema_request_key:
            request_body[self.parent_key][schema_request_key] = schema_url
        
        self._append_kwargs(request_body, **kwargs)
        response = api_call.post(self.base_url + (self.api_path).format(domain=self.domain), auth=self.auth, data=request_body)
        return request_body[self.parent_key]


    def create_transform_action(self, stylesheet_path,  name=None, rule_name=None, stylesheet_parameters=None, uid=None, **kwargs):
        """Creates a new ``transform action``

        Parameters:
            name (str): The name of the action
            stylesheet_path (str): The stylesheet location on DataPower
            stylesheet_parameters (dict): A dict contains stylesheet parameters' names and their valuse - {"param1": "value", ... }
            rule_name (str): The name of the rule which the new validate action would be attached to

        Returns:
            dict: a dict/json object of the new transform action
        """
        request_body = deepcopy(transform_action_request_body)
        request_body[self.parent_key]["name"] =  self.create_name_by_convention(rule_name, "xform", uid) if rule_name != None and name == None else name
        name = request_body[self.parent_key]["name"]
        request_body[self.parent_key]["Transform"] = stylesheet_path
        if stylesheet_parameters != None:
            request_body[self.parent_key]["StylesheetParameters"] = [{ "ParameterName": "{http://www.datapower.com/param/config}" + key, "ParameterValue": stylesheet_parameters[key] } for key in stylesheet_parameters.keys()]
        self._append_kwargs(request_body, **kwargs)

        response = api_call.post(self.base_url + (self.api_path).format(domain=self.domain), auth=self.auth, data=request_body)
        return request_body[self.parent_key]


    def create_gateway_script_action(self, gateway_script_path,  name=None, rule_name=None, stylesheet_parameters={}, uid=None, **kwargs):
        """Creates a new ``gateway script action``

        Parameters:
            name (str): The name of the action
            gateway_script_path (str): The gateway script location on DataPower
            stylesheet_parameters (dict): A dict contains stylesheet parameters' names and their valuse - {"param1": "value", ... }
            rule_name (str): The name of the rule which the new validate action would be attached to

        Returns:
            dict: a dict/json object of the new gateway script action
        """
        request_body = deepcopy(gateway_script_action_request_body)
        request_body[self.parent_key]["name"] =  self.create_name_by_convention(rule_name, "gatewayscript", uid) if rule_name != None and name == None else name
        name = request_body[self.parent_key]["name"]
        request_body[self.parent_key]["GatewayScriptLocation"] = gateway_script_path
        request_body[self.parent_key]["StylesheetParameters"] = [{ "ParameterName": "{http://www.datapower.com/param/config}" + key, "ParameterValue": stylesheet_parameters[key] } for key in stylesheet_parameters.keys()]
        self._append_kwargs(request_body, **kwargs)

        response = api_call.post(self.base_url + (self.api_path).format(domain=self.domain), auth=self.auth, data=request_body)
        return request_body[self.parent_key]


    def create_results_action(self, name=None, rule_name=None, action_input="INPUT", uid=None, **kwargs):
        """Creates a new ``result action``

        Parameters:
            name (str): The name of the action
            action_input (str): input of the action
            rule_name (str): The name of the rule which the new validate action would be attached to

        Returns:
            dict: a dict/json object of new result action
        """
        request_body = deepcopy(result_action_request_body)
        request_body[self.parent_key]["name"] =  self.create_name_by_convention(rule_name, "results", uid) if rule_name != None and name == None else name
        name = request_body[self.parent_key]["name"]
        request_body[self.parent_key]["Input"] = action_input
        self._append_kwargs(request_body, **kwargs)

        response = api_call.post(self.base_url + (self.api_path).format(domain=self.domain), auth=self.auth, data=request_body)
        return request_body[self.parent_key]
    

    def create_slm_action(self, statements, name=None, rule_name=None, action_input="INPUT", uid=None, **kwargs):
        """Creates a new ``slm action``

        Parameters:
            name (str): The name of the action
            statements (list): A list of slm policy statements.
            
            [
                {
                    "action": "throttle",
                    "interval": 1,
                    "interval_type": "moving",
                    "threshold_algorithm": "greater-than",
                    "threshold_type": "payload-total",
                    "threshold_level": "10"
                }
            ]
            
            rule_name (str): The name of the rule which the new validate action would be attached to

        Returns:
            dict: a dict/json object of new result action
        """

        request_body = deepcopy(slm_action_request_body)
        request_body[self.parent_key]["name"] =  self.create_name_by_convention(rule_name, "slm", uid) if rule_name != None and name == None else name
        name = request_body[self.parent_key]["name"]

        # Creating slm policy using slm endpoint
        slm = SLM(self.auth, self.base_url, self.domain)
        slm_policy = slm.create("{rule_name}_SLM_policy".format(rule_name=rule_name), statements)
        request_body[self.parent_key]["SLMPolicy"] = slm_policy["name"]
        request_body[self.parent_key]["Input"] = action_input
        self._append_kwargs(request_body, **kwargs)
        
        response = api_call.post(self.base_url + (self.api_path).format(domain=self.domain), auth=self.auth, data=request_body)
        return request_body[self.parent_key]


    def create_name_by_convention(self, rule_name, action_type, uid=None):
        if uid == None:  
            uid = str(uuid.uuid4())[:8] 
        return "{rule_name}_{action}_{id}".format(rule_name=rule_name, action=action_type, id=uid)


