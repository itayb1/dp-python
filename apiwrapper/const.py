API_PATH = {
    "http_handler": "mgmt/config/{domain}/HTTPSourceProtocolHandler",
    "mq_handler": "mgmt/config/{domain}/MQSourceProtocolHandler",
    "mpgw": "mgmt/config/{domain}/MultiProtocolGateway",
    "policy_attachments": "mgmt/config/{domain}/PolicyAttachments",
    "style_policy": "mgmt/config/{domain}/StylePolicy",
    "style_policy_action": "mgmt/config/{domain}/StylePolicyAction",
    "style_policy_rule": "mgmt/config/{domain}/StylePolicyRule",
    "match_action": "mgmt/config/{domain}/Matching"
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
        "StylesheetParameters": {
            "ParameterName": "{http://www.datapower.com/param/config}to",
            "ParameterValue": "http://google.com"
        },
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
