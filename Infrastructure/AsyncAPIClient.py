import asyncio
import json

import aiohttp

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

asyncio.Semaphore(2500)


class AsyncAPIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    async def _make_request(self, method, endpoint: str, payload: dict = None):
        async with aiohttp.ClientSession() as session:
            print(f"Making Request: {self.base_url}{endpoint}\nPayload: {payload}\n\n")
            async with session.request(method, f"{self.base_url}{endpoint}", json=payload) as response:
                data = await response.json()
                status_code = response.status
                return {"response_data": data, "status_code": status_code}

    async def async_get_request(self, endpoint: str, payload: dict = None):
        return await self._make_request("GET", endpoint, payload)

    async def async_post_request(self, endpoint: str, payload: dict = None):
        return await self._make_request("POST", endpoint, payload)

    async def async_handle_requests(self, tasks):
        # return self._beautify_responses(await asyncio.gather(*tasks))
        if not hasattr(tasks, '__iter__'):
            return await asyncio.gather(*[tasks])
        else: return await asyncio.gather(*tasks)


############### We can add this method and beautify the responses, BE AWARE that the status code can be part of the entire data object which can cause confusion #################
    # def _beautify_responses(self, responses_list):
    #     beautified_response_list = []
    #     for response in responses_list:
    #         beautified_response = {}
    #         for key, value in response.items():
    #             if isinstance(value, dict):
    #                 for inner_key, data in value.items():
    #                     beautified_response[f"{inner_key}"] = data
    #             else:
    #                 beautified_response[f"{key}"] = value
    #         beautified_response_list.append(beautified_response)
    #     return beautified_response_list
###################################################################################################################################################################################


# Example usage:
async def main():
    payloads = [{
        "name": "morpheus",
        "job": "leader"
    }, {
        "name": "Chara",
        "job": "leader"
    }]
    async_api_client = AsyncAPIClient("https://reqres.in/api/")
    post_req_data = await async_api_client.async_handle_requests(
        async_api_client.async_post_request(f"users", payload) for payload in payloads)

    get_req_data = await async_api_client.async_handle_requests(
        async_api_client.async_get_request(f"users/1"))
    print(json.dumps(post_req_data, indent=4))
    print(json.dumps(get_req_data, indent=4))


asyncio.run(main())
