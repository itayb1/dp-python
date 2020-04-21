from .const import API_PATH, slm_policy, slm_policy_statement
from .base import api_call
from copy import deepcopy
from .DPEndpoint import DPEndpoint


class SLM(DPEndpoint):
    def __init__(self, auth, base_url, domain):
        DPEndpoint.__init__(self, auth=auth, base_url=base_url, domain=domain)
        self.parent_key = "SLMPolicy"
        self.api_path = API_PATH["slm"]


    def create(self, name, statements, **kwargs):
        """Creates a new ``slm policy``

            Parameters:
                name (str): The name of the slm policy
                statements (list): A list of slm policy statements.

                [
                    {
                        "action": "throttle",
                        "interval": 1,
                        "intervalType": "moving",
                        "thresholdAlgorithm": "greater-than",
                        "thresholdType": "payload-total",
                        "thresholdlLevel": "10"
                    }
                ]

            Returns:
                dict: a dict/json object of new style policy rule
        """
        request_body = deepcopy(slm_policy)
        request_body[self.parent_key]["name"] = name
        for i,statement in enumerate(statements):
            statement = self.__create_slm_policy_statement(i, statement["action"], statement["interval"], statement["intervalType"],
                                                           statement["thresholdAlgorithm"], statement["thresholdType"], statement["thresholdLevel"])
            request_body[self.parent_key]["Statement"].append(statement)

        self._append_kwargs(request_body, **kwargs)
        response = api_call.post(self.base_url + (self.api_path).format(domain=self.domain), auth=self.auth, data=request_body)
        return request_body[self.parent_key]


    def __create_slm_policy_statement(self, slm_id, action, interval, interval_type, threshold_algorithm, threshold_type, threshold_level, **kwargs):
        request_body = deepcopy(slm_policy_statement)

        request_body["SLMId"] = slm_id
        request_body["Action"]["value"] = action
        request_body["ThreshIntervalLength"] = interval
        request_body["ThresholdLevel"] = threshold_level
        request_body["ThreshIntervalType"] = interval_type
        request_body["ThreshAlgorithm"] = threshold_algorithm
        request_body["ThresholdType"] = threshold_type
        self._append_kwargs(request_body, **kwargs)

        return request_body
