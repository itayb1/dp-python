from .const import API_PATH, validate_action_request_body, transform_action_request_body, result_action_request_body, match_request_body, match_rule_request_body
from .base import api_call
from .DPEndpoint import DPEndpoint


class Action(DPEndpoint):
    def __init__(self, auth, base_url, domain):
        DPEndpoint.__init__(self, auth=auth, base_url=base_url, domain=domain)
        self.type = None
        self.rule_name = None
        self.parent_key = "StylePolicyAction"
        self.api_path = API_PATH["style_policy_action"]

    def create(self):
        pass
    

    def append_kwargs(self, request_body, kwargs):
        for key in kwargs.keys():
            request_body["StylePolicyAction"][key] = kwargs[key]
    

    def create_name_by_convention(self, rule_name):
        return "{rule_name}_{action}".format(rule_name=rule_name, action=self.type)


class ValidateAction(Action):
    def __init__(self, base_url, auth, domain):
        Action.__init__(self, base_url=base_url, auth=auth, domain=domain)
        self.type = "validate"
        self.schema_types = {"json": "JSONSchemaURL", "xml": "SchemaURL"}


    def create(self, schema_url, schema_type, name=None, rule_name=None, **kwargs):
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
        request_body["StylePolicyAction"]["name"] = self.create_name_by_convention(rule_name) if (rule_name != None and name == None) else name
        name = request_body["StylePolicyAction"]["name"]
        schema_request_key = self.schema_types.get(schema_type.lower())
        if schema_request_key:
            request_body["StylePolicyAction"][schema_request_key] = schema_url
        
        self.append_kwargs(request_body, kwargs)
        response = api_call.put(self.base_url + (self.api_path+"/{name}").format(domain=self.domain, name=name), auth=self.auth, data=request_body)
        return request_body["StylePolicyAction"]


class TransformAction(Action):
    def __init__(self, base_url, auth, domain):
        Action.__init__(self, base_url=base_url, auth=auth, domain=domain)
        self.type = "xform"


    def create(self, stylesheet_path,  name=None, rule_name=None, stylesheet_parameters={}, **kwargs):
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
        request_body["StylePolicyAction"]["name"] =  self.create_name_by_convention(rule_name) if rule_name != None and name == None else name
        name = request_body["StylePolicyAction"]["name"]
        request_body["StylePolicyAction"]["Transform"] = stylesheet_path
        request_body["StylePolicyAction"]["StylesheetParameters"] = [{ "ParameterName": "{http://www.datapower.com/param/config}" + key, "ParameterValue": stylesheet_parameters[key] } for key in stylesheet_parameters.keys()]

        for key,value in kwargs.items():
            request_body["StylePolicyAction"][key] = value

        response = api_call.put(self.base_url + (self.api_path+"/{name}").format(domain=self.domain, name=name), auth=self.auth, data=request_body)
        return request_body["StylePolicyAction"]


class MatchAction(Action):
    def __init__(self, base_url, auth, domain):
        Action.__init__(self, base_url=base_url, auth=auth, domain=domain)
        self.type = "match"
        self.parent_key = "Matching"
        self.api_path = API_PATH["match_action"]
    

    def create(self, match_rules,  name=None, rule_name=None,  match_with_pcre="off", combine_with_or="off"):
        """Creates a new ``match action``

            Parameters:
            name (str): The name of the action
            rule_name (str): The name of the rule which the new validate action would be attached to
            match_rules (list): A list of json/dict objects representing match rules to be applied to the match action

            Examples:
            match_rule json object:
            {
                "Type": "url",
                "HttpTag": "",
                "HttpValue": "",
                "Url": "*",
                "ErrorCode": "",
                "XPATHExpression": "",
                "Method": "default",
                "CustomMethod": ""
            }

            Returns:
            dict: a dict/json object of the new match action
        """
        request_body = match_request_body.copy()
        request_body["Matching"]["name"] =  self.create_name_by_convention(rule_name) if rule_name != None and name == None else name
        name = request_body["Matching"]["name"]
        request_body["Matching"]["name"] = name
        request_body["Matching"]["MatchRules"] = match_rules
        request_body["Matching"]["MatchWithPCRE"] = match_with_pcre
        request_body["Matching"]["CombineWithOr"] = combine_with_or

        response =  api_call.put(self.base_url + (self.api_path+"/{name}").format(domain=self.domain, name=name), auth=self.auth, data=request_body)
        return request_body["Matching"]


    @staticmethod
    def create_match_rule(match_type, url="", http_tag="", http_value="", error_code="", xpath="", method="", custom_method=""):
        match_rule_obj = match_rule_request_body.copy()
        match_rule_obj["Type"] = match_type
        match_rule_obj["HttpTag"] = http_tag
        match_rule_obj["HttpValue"] = http_value
        match_rule_obj["Url"] = url
        match_rule_obj["ErrorCode"] = error_code
        match_rule_obj["XPATHExperssion"] = xpath
        match_rule_obj["Method"] = method
        match_rule_obj["CustomMethod"] = custom_method

        return match_rule_obj
    

    @staticmethod
    def generate_mq_url_match(front_handler, get_queue, queue_manager):
        return "dpmq://{queue_manager}/{front_handler}?RequestQueue={get_queue}".format(queue_manager=queue_manager, front_handler=front_handler, get_queue=get_queue)
        

class ResultAction(Action):
    def __init__(self, base_url, auth, domain):
        Action.__init__(self, base_url=base_url, auth=auth, domain=domain)
        self.type = "results"

    def create(self, name=None, rule_name=None, action_input="INPUT", **kwargs):
        """Creates a new ``result action``

        Parameters:
            name (str): The name of the action
            action_input (str): input of the action
            rule_name (str): The name of the rule which the new validate action would be attached to

        Returns:
            dict: a dict/json object of new result action
        """
        request_body = result_action_request_body.copy()
        request_body["StylePolicyAction"]["name"] =  self.create_name_by_convention(rule_name) if rule_name != None and name == None else name
        name = request_body["StylePolicyAction"]["name"]
        request_body["StylePolicyAction"]["Input"] = action_input
        

        self.append_kwargs(request_body, kwargs)

        response = api_call.put(self.base_url + (self.api_path+"/{name}").format(domain=self.domain, name=name), auth=self.auth, data=request_body)
        return request_body["StylePolicyAction"]




			