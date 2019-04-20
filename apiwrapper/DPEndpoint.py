from .base import api_call
from collections import MutableMapping


class DPEndpoint():
    def __init__(self, auth, base_url, domain):
        self.auth = auth
        self.base_url = base_url
        self.domain = domain
        self._append_domain = lambda uri: uri.format(domain=self.domain)
        self.parent_key = None
        self.api_path = None


    def append_kwargs(self, request_name, request_body, kwargs):
        for key,value in kwargs:
            request_body[request_name][key] = value


    @staticmethod
    def __delete_keys_from_dict(dictionary, keys):
        keys_set = set(keys)  # Just an optimization for the "if key in keys" lookup.

        modified_dict = {}
        for key, value in dictionary.items():
            if key not in keys_set:
                if isinstance(value, MutableMapping):
                    modified_dict[key] = DPEndpoint.__delete_keys_from_dict(value, keys_set)
                else:
                    modified_dict[key] = value  # or copy.deepcopy(value) if a copy is desired for non-dicts.
        return modified_dict


    @staticmethod
    def __work_fields(fields, **fieldargs):
        if fields != None:
            return fields
        elif fieldargs != None:
            return fieldargs
        else:
            return {}


    def __update_dict_values(self, obj, new_dict):
        for key in new_dict.keys():
            if  isinstance(new_dict[key], dict):
                self.__update_dict_values(obj[key], new_dict[key])
            else:
                obj[key] = new_dict.get(key)


    def update(self, obj, fields=None, **fieldargs):
        """Updates a dp object

        Each keyword argument (other than the predefined ones) is treated as a field name and the argument's value
        is treated as the intended value for that field -- if the fields argument is used, all other keyword arguments
        will be ignored.

        Parameters:
            obj (dict): A dict/json object of the dp object we want to update
            fields (dict): A dict containing field names and the values to use. If present, all other keyword arguments will be ignored

        Returns:
            dict: a dict/json object of the requested dp object
        """
        data = DPEndpoint.__work_fields(fields, **fieldargs)
        self.__update_dict_values(obj, data)
        request_body = { self.parent_key : obj }
        response = api_call.put(self.base_url + (self.api_path+"/{name}").format(domain=self.domain, name=obj["name"]), auth=self.auth, data=request_body)
        return obj 


    def get(self, name):
        """Gets a dp object

        Parameters:
            name (str): The name of the dp object 

        Returns:
            dict: a dict/json object of the requested dp object
        """
        full_request_url = "{base_url}{endpoint}/{name}".format(base_url=self.base_url, endpoint=self._append_domain(self.api_path), name=name)
        response = api_call.get(full_request_url, auth=self.auth)[self.parent_key]
        return DPEndpoint.__delete_keys_from_dict(response, ["href"])
        
