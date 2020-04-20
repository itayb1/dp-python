from .SourceHandlers import HTTPHandler, MQHandler
from .StylePolicy import StylePolicy
from .Action import Action
from .Rule import Rule
from .MPGW import MPGW
from .Matching import Matching
from .status import Status
from .xml_manager import XmlManager
from .load_balancer_group import LoadBalanacerGroup
from .slm import SLM

class DpAPI():
    def __init__(self, base_url, auth, domain):
        self.http_handler = HTTPHandler(base_url=base_url, auth=auth, domain=domain)
        self.mq_handler = MQHandler(base_url=base_url, auth=auth, domain=domain)
        self.mpgw = MPGW(base_url=base_url, auth=auth, domain=domain)
        self.style_policy = StylePolicy(base_url=base_url, auth=auth, domain=domain)
        self.rule = Rule(base_url=base_url, auth=auth, domain=domain)
        self.matching = Matching(base_url=base_url, auth=auth, domain=domain)
        self.action = Action(base_url=base_url, auth=auth, domain=domain)
        self.status = Status(base_url=base_url, auth=auth, domain=domain)
        self.xml_manager = XmlManager(base_url=base_url, auth=auth, domain=domain)
        self.lbg = LoadBalanacerGroup(base_url=base_url, auth=auth, domain=domain)
        self.slm = SLM(base_url=base_url, auth=auth, domain=domain)
        