import asyncio
import json

import aiohttp

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

asyncio.Semaphore(2500)
class AsyncAPIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    async def async_get_request(self, endpoint: str, payload: dict = None):
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=2500)) as session:
            async with session.get(f"{self.base_url}{endpoint}", json=payload) as response:
                data = await response.json()
                status_code = response.status
                return {"data": data, "status_code": status_code}

    async def async_handle_requests(self, tasks):
        return await asyncio.gather(*tasks)

    def beautify_responses(self, responses_list):
        beautified_response_list =[]
        for response in responses_list:
            beautified_response = {}
            for key, value in response.items():
                if isinstance(value, dict):
                    for inner_key, data in value.items():
                        beautified_response[f"{inner_key}"] = data
                else: beautified_response[f"{key}"] = value
            beautified_response_list.append(beautified_response)
        return beautified_response_list
# Example usage:
async def main():
    payloads = [{"data1": "some_data1"}, {"data2": "some_data2"}]
    async_api_client = AsyncAPIClient("https://reqres.in/api/")
    responses_list =await async_api_client.async_handle_requests(async_api_client.async_get_request(f"users/{index}") for index in range(1,746))
    data = async_api_client.beautify_responses(responses_list)
    print(json.dumps(data, indent=4))

asyncio.run(main())