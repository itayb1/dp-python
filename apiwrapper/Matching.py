from .const import API_PATH, rule_request_body
from .base import api_call
from .DPEndpoint import DPEndpoint

class Matching(DPEndpoint):
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
        request_body["Matching"]["name"] =  self.create_name_by_convention(rule_name, "match") if rule_name != None and name == None else name
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


    def create_name_by_convention(self, rule_name, action_type):
        return "{rule_name}_{action}".format(rule_name=rule_name, action=action_type)
