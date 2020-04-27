from .const import API_PATH
from .base import api_call
from copy import deepcopy
from .DPEndpoint import DPEndpoint


class FileStore(DPEndpoint):
    def __init__(self, auth, base_url, domain):
        DPEndpoint.__init__(self, auth=auth, base_url=base_url, domain=domain)
        self.parent_key = "filestore"
        self.api_path = API_PATH["filestore"]


    def get(self):
        full_request_url = "{base_url}{endpoint}".format(base_url=self.base_url, endpoint=self._append_domain(self.api_path))
        response = api_call.get(full_request_url, auth=self.auth)[self.parent_key]
        return DPEndpoint._delete_keys_from_dict(response, ["href"])

   
    def get_dirlist(self, parent_directory, sub_directory=None):
        url = "{base_url}{endpoint}/{sub}" if sub_directory else "{base_url}{endpoint}"
        full_request_url = url.format(base_url=self.base_url, endpoint="{}/{}".format(self._append_domain(self.api_path),parent_directory), sub=sub_directory)
        response = api_call.get(full_request_url, auth=self.auth)[self.parent_key]
        return DPEndpoint._delete_keys_from_dict(response, ["href"])

    
    def get_directory_list(self, parent_directory, sub_directory=None):
        dirlist = self.get_dirlist(parent_directory, sub_directory)
        directories = dirlist["location"].get("directory")
        if directories:
            if isinstance(directories, list):
                return [dir["name"].replace("{}:/".format(parent_directory), "") for dir in directories]
            elif isinstance(directories, dict):
                return [directories["name"].replace("{}:/".format(parent_directory), "")]
        return None


    def get_filelist(self, parent_directory, sub_directory=None, full_path=False):
        dirlist = self.get_dirlist(parent_directory, sub_directory)
        files = dirlist["location"]["file"]
        url = "{p}:///{s}/{n}" if sub_directory else "{p}:///{n}"
        if isinstance(files, list):
            if full_path:
                return [url.format(p=parent_directory, s=sub_directory, n=f["name"]) for f in files]
            return [f["name"] for f in files]
        elif isinstance(files, dict):
            if full_path:
                return [url.format(p=parent_directory, s=sub_directory, n=files["name"])]
            return [files["name"]]
    

    def get_filelist_recursive(self, parent_directory, sub_directory=None):
        dirs = self.get_directory_list(parent_directory, sub_directory)
        files = self.get_filelist(parent_directory, sub_directory, full_path=True)
        if dirs == None:
            return files
        else:
            all_files = files
            for directory in dirs:
               all_files += self.get_filelist_recursive(parent_directory, directory) 
            return all_files






