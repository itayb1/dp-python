API_PATH = {
    "http_handler": "mgmt/config/{domain}/HTTPSourceProtocolHandler",
    "mq_handler": "mgmt/config/{domain}/MQSourceProtocolHandler",
    "mpgw": "mgmt/config/{domain}/MultiProtocolGateway",
    "policy_attachments": "mgmt/config/{domain}/PolicyAttachments",
    "style_policy": "mgmt/config/{domain}/StylePolicy",
    "style_policy_action": "mgmt/config/{domain}/StylePolicyAction",
    "style_policy_rule": "mgmt/config/{domain}/StylePolicyRule",
    "match_action": "mgmt/config/{domain}/Matching",
    "xml_manager": "mgmt/config/{domain}/XMLManager",
    "load_balancer_group": "mgmt/config/{domain}/LoadBalancerGroup",
    "status": "mgmt/status/{domain}"

}


##########################################################
######                                              ######
######                Front Handlers                ######
######                                              ######
##########################################################

http_features = {
    "HTTP-1.0": "on",
    "HTTP-1.1": "on",
    "HTTP-2.0": "off",
    "POST": "off",
    "GET": "off",
    "PUT": "off",
    "HEAD": "off",
    "OPTIONS": "off",
    "TRACE": "off",
    "DELETE": "off",
    "CONNECT": "off",
    "CustomMethods": "off",
    "QueryString": "on",
    "FragmentIdentifiers": "on",
    "DotDot": "off",
    "CmdExe": "off"
}

mq_source_handler_request_body = {
    "MQSourceProtocolHandler": {
        "name": None,
        "mAdminState": "enabled",
        "QueueManager": {
            "value": None,
        },
        "GetQueue": "Best_MQ_2",
        "CodePage": 0,
        "GetMessageOptions": 1,
        "ParseProperties": "on",
        "AsyncPut": "off",
        "ConcurrentConnections": 1,
        "PollingInterval": 30,
        "BatchSize": 0,
        "RetrieveBackoutSettings": "off",
        "UseQMNameInURL": "off"
    }
}

http_source_handler_request_body = {
    "HTTPSourceProtocolHandler": {
        "name": None,
        "mAdminState": "enabled",
        "LocalAddress": "eth0_ipv4_1",
        "LocalPort": 80,
        "HTTPVersion": "HTTP/1.1",
        "AllowedFeatures": http_features,
        "PersistentConnections": "on",
        "MaxPersistentConnectionsReuse": 0,
        "AllowCompression": "off",
        "AllowWebSocketUpgrade": "off",
        "WebSocketIdleTimeout": 0,
        "MaxURLLen": 16384,
        "MaxTotalHdrLen": 128000,
        "MaxHdrCount": 0,
        "MaxNameHdrLen": 0,
        "MaxValueHdrLen": 0,
        "MaxQueryStringLen": 0,
        "CredentialCharset": "protocol",
        "HTTP2MaxStreams": 100,
        "HTTP2MaxFrameSize": 16384,
        "HTTP2StreamHeader": "off",
        "ChunkedEncoding": "on"
    }
}

mq_exclude_headers = {
    "MQCIH": "off",
    "MQDLH": "off",
    "MQIIH": "off",
    "MQRFH": "off",
    "MQRFH2": "off",
    "MQWIH": "off"
}


##########################################################
######                                              ######
######                    MPGW                      ######
######                                              ######
##########################################################

MPGW_request_body = {
    "MultiProtocolGateway": {
        "name": None,
        "mAdminState": None,
        "Priority": "normal",
        "FrontProtocol": None,
        "XMLManager": None,
        "StylePolicy": None,
        "PolicyAttachments": None,
        "SSLClientConfigType": "proxy",
        "DefaultParamNamespace": "http://www.datapower.com/param/config",
        "QueryParamNamespace": "http://www.datapower.com/param/query",
        "PropagateURI": "on",
        "MonitorProcessingPolicy": "terminate-at-first-throttle",
        "RequestAttachments": "strip",
        "ResponseAttachments": "strip",
        "RequestAttachmentsFlowControl": "off",
        "ResponseAttachmentsFlowControl": "off",
        "RootPartNotFirstAction": "process-in-order",
        "FrontAttachmentFormat": "dynamic",
        "BackAttachmentFormat": "dynamic",
        "MIMEFrontHeaders": "on",
        "MIMEBackHeaders": "on",
        "StreamOutputToBack": "buffer-until-verification",
        "StreamOutputToFront": "buffer-until-verification",
        "MaxMessageSize": 0,
        "GatewayParserLimits": "off",
        "ParserLimitsElementDepth": 512,
        "ParserLimitsAttributeCount": 128,
        "ParserLimitsMaxNodeSize": 33554432,
        "ParserLimitsExternalReferences": "forbid",
        "ParserLimitsMaxPrefixes": 1024,
        "ParserLimitsMaxNamespaces": 1024,
        "ParserLimitsMaxLocalNames": 60000,
        "ParserLimitsAttachmentByteCount": 2000000000,
        "ParserLimitsAttachmentPackageByteCount": 0,
        "DebugMode": "off",
        "DebugHistory": 25,
        "FlowControl": "off",
        "SOAPSchemaURL": "store:///schemas/soap-envelope.xsd",
        "FrontTimeout": 120,
        "BackTimeout": 120,
        "FrontPersistentTimeout": 180,
        "BackPersistentTimeout": 180,
        "IncludeResponseTypeEncoding": "off",
        "BackHTTPVersion": "HTTP/1.1",
        "PersistentConnections": "on",
        "LoopDetection": "off",
        "DoHostRewriting": "on",
        "DoChunkedUpload": "off",
        "ProcessHTTPErrors": "on",
        "HTTPClientIPLabel": "X-Client-IP",
        "HTTPLogCorIDLabel": "X-Global-Transaction-ID",
        "InOrderMode": {
            "Request": "off",
            "Backend": "off",
            "Response": "off"
        },
        "WSAMode": "sync2sync",
        "WSARequireAAA": "on",
        "WSAStrip": "on",
        "WSADefaultReplyTo": "http://schemas.xmlsoap.org/ws/2004/08/addressing/role/anonymous",
        "WSADefaultFaultTo": "http://schemas.xmlsoap.org/ws/2004/08/addressing/role/anonymous",
        "WSAForce": "off",
        "WSAGenStyle": "sync",
        "WSAHTTPAsyncResponseCode": 204,
        "WSATimeout": 120,
        "WSRMEnabled": "off",
        "WSRMSequenceExpiration": 3600,
        "WSRMDestinationAcceptCreateSequence": "on",
        "WSRMDestinationMaximumSequences": 400,
        "WSRMDestinationInOrder": "off",
        "WSRMDestinationMaximumInOrderQueueLength": 10,
        "WSRMDestinationAcceptOffers": "off",
        "WSRMFrontForce": "off",
        "WSRMBackForce": "off",
        "WSRMBackCreateSequence": "off",
        "WSRMFrontCreateSequence": "off",
        "WSRMSourceMakeOffer": "off",
        "WSRMUsesSequenceSSL": "off",
        "WSRMSourceMaximumSequences": 400,
        "WSRMSourceRetransmissionInterval": 10,
        "WSRMSourceExponentialBackoff": "on",
        "WSRMSourceMaximumRetransmissions": 4,
        "WSRMSourceMaximumQueueLength": 30,
        "WSRMSourceRequestAckCount": 1,
        "WSRMSourceInactivityClose": 360,
        "ForcePolicyExec": "off",
        "RewriteErrors": "on",
        "DelayErrors": "on",
        "DelayErrorsDuration": 1000,
        "RequestType": "preprocessed",
        "ResponseType": "preprocessed",
        "FollowRedirects": "on",
        "RewriteLocationHeader": "off",
        "Type": "dynamic-backend",
        "AllowCompression": "off",
        "AllowCacheControlHeader": "off",
        "WSMAgentMonitor": "off",
        "WSMAgentMonitorPCM": "all-messages",
        "ProxyHTTPResponse": "off",
        "TransactionTimeout": 0
    }
}

policy_attachment_request_body = {
    "PolicyAttachments": {
        "name": None,
        "mAdminState": "enabled",
        "EnforcementMode": "enforce",
        "PolicyReferences": "on",
        "SLAEnforcementMode": "allow-if-no-sla"
    }
}


##########################################################
######                                              ######
######                  Actions                     ######
######                                              ######
##########################################################

action_common_props = {
    "name": None,
    "mAdminState": "enabled",
    "Type": "results",
    "Input": "INPUT",
    "Output": "OUTPUT",
    "ParseSettingsReference": {
        "URL": "",
        "Literal": "",
        "Default": ""
    },
    "ParseMetricsResultType": "none",
    "TransformLanguage": "none",
    "ActionDebug": "off",
    "NamedInOutLocationType": "default",
    "SSLClientConfigType": "proxy",
    "Transactional": "off",
    "SOAPValidation": "body",
    "SQLSourceType": "static",
    "JWSVerifyStripSignature": "on",
    "Asynchronous": "off",
    "ResultsMode": "first-available",
    "RetryCount": 0,
    "RetryInterval": 1000,
    "MultipleOutputs": "off",
    "IteratorType": "XPATH",
    "Timeout": 0,
    "MethodRewriteType": "GET",
    "MethodType": "POST",
    "MethodType2": "POST"
}


gateway_script_action_request_body = {
    "StylePolicyAction": {
        "GatewayScriptLocation": "store:///gatewayscript/example-jwt-validate.js",
        "StylesheetParameters": {
            "ParameterName": "a",
            "ParameterValue": "aa"
        },
        "name": None,
        "mAdminState": "enabled",
        "Type": "gatewayscript",
        "Input": "INPUT",
        "Output": "OUTPUT",
        "ParseSettingsReference": {
            "URL": "",
            "Literal": "",
            "Default": ""
        },
        "ParseMetricsResultType": "none",
        "TransformLanguage": "none",
        "ActionDebug": "off",
        "NamedInOutLocationType": "default",
        "SSLClientConfigType": "proxy",
        "Transactional": "off",
        "SOAPValidation": "body",
        "SQLSourceType": "static",
        "JWSVerifyStripSignature": "on",
        "Asynchronous": "off",
        "ResultsMode": "first-available",
        "RetryCount": 0,
        "RetryInterval": 1000,
        "MultipleOutputs": "off",
        "IteratorType": "XPATH",
        "Timeout": 0,
        "MethodRewriteType": "GET",
        "MethodType": "POST",
        "MethodType2": "POST"
    }
}


validate_action_request_body = {
    "StylePolicyAction": {
        "name": None,
        "mAdminState": "enabled",
        "Type": "validate",
        "Input": "INPUT",
        "ParseSettingsReference": {
                "URL": "",
                "Literal": "",
                "Default": ""
        },
        "ParseMetricsResultType": "none",
        "TransformLanguage": "none",
        "ActionDebug": "off",
        "NamedInOutLocationType": "default",
        "SSLClientConfigType": "proxy",
        "Transactional": "off",
        "SOAPValidation": "body",
        "SQLSourceType": "static",
        "JWSVerifyStripSignature": "on",
        "Asynchronous": "off",
        "ResultsMode": "first-available",
        "RetryCount": 0,
        "RetryInterval": 1000,
        "MultipleOutputs": "off",
        "IteratorType": "XPATH",
        "Timeout": 0,
        "MethodRewriteType": "GET",
        "MethodType": "POST",
        "MethodType2": "POST"
    }
}

transform_action_request_body = {
    "StylePolicyAction": {
        "name": None,
        "Type": "xform",
        "mAdminState": "enabled",
        "Input": "NULL",
        "Output": "NULL",
        "Transform": "store:///soap-mediation.xsl",
        "OutputType": "default",
        "ParseSettingsReference": {
            "URL": "",
            "Literal": "",
            "Default": ""
        },
        "ParseMetricsResultType": "none",
        "TransformLanguage": "none",
        "ActionDebug": "off",
        "NamedInOutLocationType": "default",
        "SSLClientConfigType": "proxy",
        "Transactional": "off",
        "SOAPValidation": "body",
        "SQLSourceType": "static",
        "JWSVerifyStripSignature": "on",
        "Asynchronous": "off",
        "ResultsMode": "first-available",
        "RetryCount": 0,
        "RetryInterval": 1000,
        "MultipleOutputs": "off",
        "IteratorType": "XPATH",
        "Timeout": 0,
        "MethodRewriteType": "GET",
        "MethodType": "POST",
        "MethodType2": "POST"
    }
}

result_action_request_body = {
    "StylePolicyAction": {
        "name": None,
        "mAdminState": "enabled",
        "Type": "results",
        "Input": "INPUT",
        "ParseSettingsReference": {
            "URL": "",
            "Literal": "",
            "Default": ""
        },
        "OutputType": "default",
        "ParseMetricsResultType": "none",
        "TransformLanguage": "none",
        "ActionDebug": "off",
        "NamedInOutLocationType": "default",
        "SSLClientConfigType": "proxy",
        "Transactional": "off",
        "SOAPValidation": "body",
        "SQLSourceType": "static",
        "JWSVerifyStripSignature": "on",
        "Asynchronous": "off",
        "ResultsMode": "first-available",
        "RetryCount": 0,
        "RetryInterval": 1000,
        "MultipleOutputs": "off",
        "IteratorType": "XPATH",
        "Timeout": 0,
        "MethodRewriteType": "GET",
        "MethodType": "POST",
        "MethodType2": "POST"
    }
}


##########################################################
######                                              ######
######            StylePolicy and Rules             ######
######                                              ######
##########################################################


style_policy_request_body = {
    "StylePolicy": {
        "name": None,
        "mAdminState": "enabled",
        "DefStylesheetForSoap": "store:///filter-reject-all.xsl",
        "DefStylesheetForXsl": "store:///identity.xsl",
        "DefXQueryForJSON": "store:///reject-all-json.xq",
        "PolicyMaps": None
    }
}

rule_request_body = {
    "StylePolicyRule": {
        "name": None,
        "mAdminState": "enabled",
        "Actions": None,
        "Direction": None,
        "InputFormat": "none",
        "OutputFormat": "none",
        "NonXMLProcessing": "off",
        "Unprocessed": "off"
    }
}


# Match

match_request_body = {
    "Matching": {
        "name": None,
        "mAdminState": "enabled",
        "MatchRules": None,
        "MatchWithPCRE": "off",
        "CombineWithOr": "off"
    }
}

match_rule_request_body = {
    "Type": "url",
    "HttpTag": "",
    "HttpValue": "",
    "Url": "*",
    "ErrorCode": "",
    "XPATHExpression": "",
    "Method": "default",
    "CustomMethod": ""
}


xml_manager_request_body = {
    "XMLManager": {
        "name": None,
        "mAdminState": "enabled",
        "UserSummary": "Default XML-Manager",
        "CacheSize": 256,
        "SHA1Caching": "on",
        "StaticDocumentCalls": "on",
        "SearchResults": "on",
        "SupportTxWarn": "off",
        "ParserLimitsBytesScanned": 4194304,
        "ParserLimitsElementDepth": 512,
        "ParserLimitsAttributeCount": 128,
        "ParserLimitsMaxNodeSize": 33554432,
        "ParserLimitsExternalReferences": "forbid",
        "ParserLimitsMaxPrefixes": 1024,
        "ParserLimitsMaxNamespaces": 1024,
        "ParserLimitsMaxLocalNames": 60000,
        "DocCacheMaxDocs": 5000,
        "DocCacheSize": 0,
        "DocMaxWrites": 32768,
        "UserAgent": {
            "value": "default"
        }
    }
}


load_balancer_group_tcpconnection = {
    "LoadBalancerGroup": {
        "name": "test_lbg2",
        "mAdminState": "enabled",
        "Algorithm": "round-robin",
        "RetrieveInfo": "off",
        "WLMRetrieval": "use-websphere",
        "WLMTransport": "http",
        "Damp": 120,
        "NeverReturnSickMember": "off",
        "LBGroupMembers": [{
                "Server": "127.0.0.1",
                "Weight": 1,
                "MappedPort": 9000,
                "Activity": "",
                "HealthPort": "",
                "LBMemberState": "enabled"
        }],
        "TryEveryServerBeforeFailing": "off",
        "LBGroupChecks": {
            "Active": "on",
            "URI": "/",
            "Port": 9000,
            "SSL": "TCPConnection",
            "Post": "on",
            "Input": "store:///healthcheck.xml",
            "Timeout": 10,
            "Frequency": 180,
            "XPath": "/",
            "Filter": "store:///healthcheck.xsl",
            "SSLProxyProfile": "",
            "EnforceTimeout": "off",
            "IndependentChecks": "off",
            "GatewayScriptChecks": "on",
            "GatewayScriptReqMethod": "GET",
            "GatewayScriptCustomReqMethod": "",
            "GatewayScriptReqDoc": "store:///healthcheck.json",
            "GatewayScriptReqContentType": "application/json",
            "GatewayScriptRspHandlerMetadata": "",
            "GatewayScriptRspHandler": "store:///healthcheck.js",
            "TCPConnectionType": "Full",
            "SSLClientConfigType": "proxy",
            "SSLClient": ""
        },
        "MasqueradeMember": "off",
        "ApplicationRouting": "off",
        "LBGroupAffinityConf": {
            "EnableSA": "on",
            "InsertionCookieName": "DPJSESSIONID",
            "InsertionPath": "/",
            "InsertionDomain": "datapower.com",
            "AffinityWLMOverride": "off",
            "AffinityMode": "activeConditional",
            "InsertionAttributes": {
                "secure": "off",
                "httponly": "off"
            }
        }
    }
}


load_balancer_group_standard = {
    "LoadBalancerGroup": {
        "name": "test_lbg",
        "mAdminState": "enabled",
        "Algorithm": "round-robin",
        "RetrieveInfo": "off",
        "WLMRetrieval": "use-websphere",
        "WLMTransport": "http",
        "Damp": 120,
        "NeverReturnSickMember": "off",
        "LBGroupMembers": [{
                "Server": "127.0.0.1",
                "Weight": 1,
                "MappedPort": 9000,
                "Activity": "",
                "HealthPort": "",
                "LBMemberState": "enabled"
        }],
        "TryEveryServerBeforeFailing": "off",
        "LBGroupChecks": {
            "Active": "on",
            "URI": "/",
            "Port": 9000,
            "SSL": "Standard",
            "Post": "on",
            "Input": "store:///healthcheck.xml",
            "Timeout": 10,
            "Frequency": 180,
            "XPath": "/",
            "Filter": "store:///healthcheck.xsl",
            "SSLProxyProfile": "",
            "EnforceTimeout": "off",
            "IndependentChecks": "off",
            "GatewayScriptChecks": "on",
            "GatewayScriptReqMethod": "GET",
            "GatewayScriptCustomReqMethod": "",
            "GatewayScriptReqDoc": "store:///healthcheck.json",
            "GatewayScriptReqContentType": "application/json",
            "GatewayScriptRspHandlerMetadata": "",
            "GatewayScriptRspHandler": "store:///healthcheck.js",
            "TCPConnectionType": "Full",
            "SSLClientConfigType": "proxy",
            "SSLClient": ""
        },
        "MasqueradeMember": "off",
        "ApplicationRouting": "off",
        "LBGroupAffinityConf": {
            "EnableSA": "on",
            "InsertionCookieName": "DPJSESSIONID",
            "InsertionPath": "/",
            "InsertionDomain": "datapower.com",
            "AffinityWLMOverride": "off",
            "AffinityMode": "activeConditional",
            "InsertionAttributes": {
                "secure": "off",
                "httponly": "off"
            }
        }
    }
}


load_balancer_group_member = {
    "Server": "127.0.0.1",
    "Weight": 1,
    "MappedPort": 9000,
    "Activity": "",
    "HealthPort": "",
    "LBMemberState": "enabled"
}
