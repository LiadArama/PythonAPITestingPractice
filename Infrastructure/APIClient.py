import requests
from Infrastructure.Logger import Logger


### This is the base class for any API class we would want to create
# It needs to have a base url, and a logger.
# we need to:
#   log the requests
#   log the response
#   handle the responses and handle errors additionally using a different error handling class
#
# Implementing a get, post, put, patch, delete methods for all other API classes, in which we can in each method:
#   Log the request
#   Log the response inside the method which handles the response
#   Handle the response inside the method we use
class APIClient():
    # init of APIClient:
        # needs a logger
        # needs a base url to work with
    def __init__(self, base_url, logger_name):
        self.base_url = base_url
        self.logger = Logger(logger_name, "APIClient")
        self.main_log = self.logger.main_logger
        self.class_logger = self.logger.class_logger

    # Log request, the method we used, and the data we used
    def _log_request(self, method, url, **kwargs): # **kwargs is like spreading a list of multiple params. can take indefinitely amount of params
        self.main_log.info(f" Method = [ {method} ] <----> URL = [ {url} ]")
        self.class_logger.info(f" Method = [ {method} ] <----> URL = [ {url} ]")
        if "params" in kwargs:
            if not kwargs["params"] is None:
                self.main_log.info(f" Request data = [ {kwargs} ]")
                self.class_logger.info(f" Request data = [ {kwargs} ]")

    # Log the response
    def _log_response(self, response):
        self.main_log.info(f" URL = [ {response.url} ] ----> Response Code = [ {response.status_code} ]" )
        self.class_logger.info(f" URL = [ {response.url} ] ----> Response Code = [ {response.status_code} ]" )

    # Handle the response
    def _handle_response(self, response):
        self._log_response(response)
        return response.json(), response.status_code

    def get_request(self, endpoint , params=None): # If needed we can supply a payload, otherwise we can specify the resource in the end of the endpoint url
        self._log_request("GET", f"{self.base_url}{endpoint}", params=params) # We MUST explicit specify params=params to let python know to reference them to **kwargs
        response = requests.get(f"{self.base_url}{endpoint}")
        return self._handle_response(response)

    def post_request(self, endpoint , payload=None): # If needed we can supply a payload, otherwise we can specify the resource in the end of the endpoint url
        self._log_request("POST", f"{self.base_url}{endpoint}", params=payload) # We MUST explicit specify params=params to let python know to reference them to **kwargs
        response = requests.post(f"{self.base_url}{endpoint}", payload)
        return self._handle_response(response)

    def put_request(self, endpoint, payload=None): # If needed we can supply a payload, otherwise we can specify the resource in the end of the endpoint url
        self._log_request("PUT", f"{self.base_url}{endpoint}", params=payload) # We MUST explicit specify params=params to let python know to reference them to **kwargs
        response = requests.put(f"{self.base_url}{endpoint}", payload)
        return self._handle_response(response)

    def patch_request(self, endpoint, payload=None): # If needed we can supply a payload, otherwise we can specify the resource in the end of the endpoint url
        self._log_request("PATCH", f"{self.base_url}{endpoint}", params=payload) # We MUST explicit specify params=params to let python know to reference them to **kwargs
        response = requests.patch(f"{self.base_url}{endpoint}", payload)
        return self._handle_response(response)

    def delete_request(self, endpoint, payload=None): # If needed we can supply a payload, otherwise we can specify the resource in the end of the endpoint url
        self._log_request("DELETE", f"{self.base_url}{endpoint}", params=payload) # We MUST explicit specify params=params to let python know to reference them to **kwargs
        response = requests.delete(f"{self.base_url}{endpoint}", payload)
        return self._handle_response(response)


