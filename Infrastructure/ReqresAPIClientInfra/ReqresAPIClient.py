from Infrastructure.APIClient  import APIClient
from Infrastructure.ReqresAPIClientInfra.ReqresAPIEndpointENUMS import ReqresAPIEndpoints

class ReqresAPIClient(APIClient):
    def __init__(self):
        super().__init__( "https://reqres.in/api/","ReqresAPIClient")

    def get_user_list_by_page_num(self, page_num):
        return self.get_request(f"{ReqresAPIEndpoints.USERS.value}?page={page_num}")

    def get_single_user(self, user_id):
        return self.get_request(f"{ReqresAPIEndpoints.USERS.value}/{user_id}")

    def update_single_user(self, user_id, payload):
        return self.put_request(f"{ReqresAPIEndpoints.USERS.value}{user_id}", payload)

    def delete_single_user(self, user_id):
        return self.delete_request(f"{ReqresAPIEndpoints.USERS.value}{user_id}")

