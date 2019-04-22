from .const import API_PATH, validate_action_request_body, transform_action_request_body, result_action_request_body, gateway_script_action_request_body
from .base import api_call
from .DPEndpoint import DPEndpoint


class Action(DPEndpoint):
    def __init__(self, auth, base_url, domain):
        DPEndpoint.__init__(self, auth=auth, base_url=base_url, domain=domain)
        self.parent_key = "StylePolicyAction"
        self.api_path = API_PATH["style_policy_action"]
        self.schema_types = {"json": "JSONSchemaURL", "xml": "SchemaURL"}


    def create(self):
        pass
    

    def create_validate_action(self, schema_url, schema_type, name=None, rule_name=None, **kwargs):
        """Creates a new ``validate action``

        Parameters:
            name (str): The name of the action
            schema_url (str): The schema location on DataPower
            schema_type (str): The schema type
            rule_name (str): The name of the rule which the new validate action would be attached to

        Returns:
            dict: a dict/json object of new validate action
        """
        request_body = validate_action_request_body.copy()
        request_body[self.parent_key]["name"] = self.__create_name_by_convention(rule_name, "validate") if (rule_name != None and name == None) else name
        name = request_body[self.parent_key]["name"]
        schema_request_key = self.schema_types.get(schema_type.lower())
        if schema_request_key:
            request_body[self.parent_key][schema_request_key] = schema_url
        
        self._append_kwargs(request_body, **kwargs)
        response = api_call.put(self.base_url + (self.api_path+"/{name}").format(domain=self.domain, name=name), auth=self.auth, data=request_body)
        return request_body[self.parent_key]


    def create_transform_action(self, stylesheet_path,  name=None, rule_name=None, stylesheet_parameters={}, **kwargs):
        """Creates a new ``transform action``

        Parameters:
            name (str): The name of the action
            stylesheet_path (str): The stylesheet location on DataPower
            stylesheet_parameters (dict): A dict contains stylesheet parameters' names and their valuse - {"param1": "value", ... }
            rule_name (str): The name of the rule which the new validate action would be attached to

        Returns:
            dict: a dict/json object of the new transform action
        """
        request_body = transform_action_request_body.copy()
        request_body[self.parent_key]["name"] =  self.__create_name_by_convention(rule_name, "xform") if rule_name != None and name == None else name
        name = request_body[self.parent_key]["name"]
        request_body[self.parent_key]["Transform"] = stylesheet_path
        request_body[self.parent_key]["StylesheetParameters"] = [{ "ParameterName": "{http://www.datapower.com/param/config}" + key, "ParameterValue": stylesheet_parameters[key] } for key in stylesheet_parameters.keys()]
        self._append_kwargs(request_body, **kwargs)

        response = api_call.put(self.base_url + (self.api_path+"/{name}").format(domain=self.domain, name=name), auth=self.auth, data=request_body)
        return request_body[self.parent_key]


    def create_gateway_script_action(self, gateway_script_path,  name=None, rule_name=None, stylesheet_parameters={}, **kwargs):
        """Creates a new ``gateway script action``

        Parameters:
            name (str): The name of the action
            gateway_script_path (str): The gateway script location on DataPower
            stylesheet_parameters (dict): A dict contains stylesheet parameters' names and their valuse - {"param1": "value", ... }
            rule_name (str): The name of the rule which the new validate action would be attached to

        Returns:
            dict: a dict/json object of the new gateway script action
        """
        request_body = gateway_script_action_request_body.copy()
        request_body[self.parent_key]["name"] =  self.__create_name_by_convention(rule_name, "gatewayscript") if rule_name != None and name == None else name
        name = request_body[self.parent_key]["name"]
        request_body[self.parent_key]["GatewayScriptLocation"] = gateway_script_path
        request_body[self.parent_key]["StylesheetParameters"] = [{ "ParameterName": "{http://www.datapower.com/param/config}" + key, "ParameterValue": stylesheet_parameters[key] } for key in stylesheet_parameters.keys()]
        self._append_kwargs(request_body, **kwargs)

        response = api_call.put(self.base_url + (self.api_path+"/{name}").format(domain=self.domain, name=name), auth=self.auth, data=request_body)
        return request_body[self.parent_key]


    def create_results_action(self, name=None, rule_name=None, action_input="INPUT", **kwargs):
        """Creates a new ``result action``

        Parameters:
            name (str): The name of the action
            action_input (str): input of the action
            rule_name (str): The name of the rule which the new validate action would be attached to

        Returns:
            dict: a dict/json object of new result action
        """
        request_body = result_action_request_body.copy()
        request_body[self.parent_key]["name"] =  self.__create_name_by_convention(rule_name, "results") if rule_name != None and name == None else name
        name = request_body[self.parent_key]["name"]
        request_body[self.parent_key]["Input"] = action_input
        self._append_kwargs(request_body, **kwargs)

        response = api_call.put(self.base_url + (self.api_path+"/{name}").format(domain=self.domain, name=name), auth=self.auth, data=request_body)
        return request_body[self.parent_key]


    def __create_name_by_convention(self, rule_name, action_type):
        return "{rule_name}_{action}".format(rule_name=rule_name, action=action_type)


