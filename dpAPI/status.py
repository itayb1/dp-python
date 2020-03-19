from .const import API_PATH, rule_request_body
from .base import api_call
from copy import deepcopy
from .DPEndpoint import DPEndpoint
from collections import Counter
import random


class Status(DPEndpoint):
    def __init__(self, auth, base_url, domain):
        DPEndpoint.__init__(self, auth=auth, base_url=base_url, domain=domain)
        self.api_path = API_PATH["status"]


    def get_free_port(self, min=1000, max=10000):
        response = api_call.get(self.base_url + self._append_domain(self.api_path) + "/TCPTable", auth=self.auth)
        tcp_table = response.get("TCPTable")
        if tcp_table:
            used_ports = sorted(set([row["localPort"] for row in tcp_table]))
            free_ports = list((Counter(list(range(min, max)))-Counter(used_ports)).elements())
            return random.choice(free_ports)
        return False


    def  is_port_free(self, port):
        response = api_call.get(self.base_url + self._append_domain(self.api_path) + "/TCPTable", auth=self.auth)
        tcp_table = response.get("TCPTable")
        if tcp_table:
            used_ports = sorted(set([row["localPort"] for row in tcp_table]))
            if port in used_ports or port > 65535:
                return False
        return True


