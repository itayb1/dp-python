from flask import Flask, request, Response, jsonify
from flask_cors import CORS
from apiwrapper import dpAPI
import json
import ast
from apiwrapper.exceptions import ApiError


app = Flask(__name__)
api = dpAPI.DpAPI("https://0.0.0.0:5554/", ("admin", "admin"), "default")
CORS(app)


@app.errorhandler(ApiError)
def handler_error(error):
    message = {
            'status': error.status_code,
            'message': error.message
    }
    resp = jsonify(message)
    resp.status_code = error.status_code
    return resp


def success_response(msg):
    message = {
        'status': 200,
        'message': msg
    }
    resp = jsonify(message)
    resp.status_code = 200
    return resp


@app.route("/", methods=['GET', 'POST'])
def hello():
    return str(dict(request.form)['name'])


@app.route("/api/mq_handler/create", methods=['post'])
def create_mq_handler():
    try:
        if request.method == "POST":
            data_dict = ast.literal_eval(request.data.decode())
            handler = api.mq_handler.create(data_dict["name"], data_dict["queue_manager"], data_dict["get_queue"], data_dict["state"])
            return success_response('MQ Handler "' + handler["name"] + '" was created')
    except ApiError as e:
        raise ApiError(e.message, e.status_code)


@app.route("/api/http_handler/create", methods=['post'])
def create_http_handler():
    try:
        if request.method == "POST":
            data_dict = ast.literal_eval(request.data.decode())
            handler = api.http_handler.create(data_dict["name"], data_dict["local_address"], data_dict["local_port"], data_dict["state"], data_dict["allowed_features"])
            return success_response('HTTP Handler "' + handler["name"] + '" was created')
    except ApiError as e:
        raise ApiError(e.message, e.status_code)


@app.route("/api/mpgw/create", methods=['post'])
def create_mpgw():
    try:
        data_dict = ast.literal_eval(request.data.decode())
        mpgw_name = data_dict["mpgw_name"]
        policy = create_style_policy(data_dict["rules"], mpgw_name)  
        api.mpgw.create(mpgw_name, front_handlers=data_dict["handlers"], xml_manager="default", style_policy=policy["name"], state="enabled")
        return success_response('mpgw "' + mpgw_name + '" was created')
    except ApiError as e:
        raise ApiError(e.message, e.status_code)


def create_rule_actions(rule_name, actions):
    try:
        rule_actions, rule_action = [], ""
        for action in actions:
            parameters = action["parameters"]
            if action["type"] == "validate":
                rule_action = api.action.create_validate_action(rule_name=rule_name, schema_url=parameters["schema_url"], schema_type=parameters["schema_type"])
            elif action["type"] == "xform":
                rule_action = api.action.create_transform_action(rule_name=rule_name, stylesheet_path=parameters["stylesheet_path"], stylesheet_parameters=parameters["stylesheet_parameters"])
            elif action["type"] == "results":
                rule_action = api.action.create_results_action(rule_name=rule_name)
            else:
                raise ApiError("Invalid action type", 400) 
            rule_actions.append(rule_action["name"])
        return rule_actions
    except ApiError as e:
        raise ApiError(e.message, e.status_code)


def create_style_policy(rules, mpgw_name):
    try:
        policy_maps = []
        for rule in rules:
            rule_name = rule["name"]
            rule_actions = create_rule_actions(rule_name, rule["actions"])        
            match_action = rule["match"]
            match_action = api.matching.create(name=match_action["name"],match_rules=match_action["match_rules"], combine_with_or=match_action["combine_with_or"], match_with_pcre=match_action["match_with_pcre"])
            policy_maps.append((match_action["name"], rule_name))
            api.rule.create(rule_name, direction=rule["direction"], actions=rule_actions)
        policy = api.style_policy.create(name="", policy_maps=policy_maps, mpgw=mpgw_name)
        return policy
    except ApiError as e:
        raise ApiError(e.message, e.status_code)
    

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=4000, debug=True)
