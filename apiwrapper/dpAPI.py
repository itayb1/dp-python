from .SourceHandlers import HTTPHandler, MQHandler
from .StylePolicy import StylePolicy
from .Action import *
from .Rule import *
from .MPGW import *

class DpAPI():
    def __init__(self, base_url, auth, domain):
        self.http_handler = HTTPHandler(base_url=base_url, auth=auth, domain=domain)
        self.mq_handler = MQHandler(base_url=base_url, auth=auth, domain=domain)
        self.mpgw = MPGW(base_url=base_url, auth=auth, domain=domain)
        self.style_policy = StylePolicy(base_url=base_url, auth=auth, domain=domain)
        self.rule = Rule(base_url=base_url, auth=auth, domain=domain)
        self.validate_action = ValidateAction(base_url=base_url, auth=auth, domain=domain)
        self.result_action = ResultAction(base_url=base_url, auth=auth, domain=domain)
        self.transform_action = TransformAction(base_url=base_url, auth=auth, domain=domain)
        self.gateway_script_action = GatewayScriptAction(base_url=base_url, auth=auth, domain=domain)
        self.match_action = MatchAction(base_url=base_url, auth=auth, domain=domain)
        