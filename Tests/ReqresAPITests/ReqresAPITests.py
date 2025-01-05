import jsonschema
import pytest
import asyncio
import requests
import aiohttp

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
from Infrastructure.ReqresAPIClientInfra.ReqresAPIClient import ReqresAPIClient
from Infrastructure.ReqresAPIClientInfra.ReqresAPIEndpointENUMS import ReqresAPIEndpoints

from Tests.ReqresAPITests.ReqresAPIJsonSchema import users_list_json_schema
from Tests.ReqresAPITests.ReqresAPIJsonSchema import single_user_jsonschema

from Tests.ReqresAPITests.ReqresAPITestsDataProvider import fetching_users_list_test_params
from Tests.ReqresAPITests.ReqresAPITestsDataProvider import fetching_single_user_test_params


# pytest -s .\ReqresAPITests.py --html-report=./report --> can use this terminal command to also generate report and print out the prints in the tests

@pytest.fixture(scope="module")
def reqres_api_client():
    reqres_api_client = ReqresAPIClient()
    yield reqres_api_client
    del reqres_api_client


@pytest.mark.parametrize("page_num, expected_status_code", fetching_users_list_test_params)
def test_fetching_users_list(reqres_api_client, page_num, expected_status_code):
    actual_data, actual_status_code = reqres_api_client.get_user_list_by_page_num(page_num)
    assert actual_status_code == expected_status_code, f"Expected Status Code: [ {expected_status_code} ], but got [{actual_status_code}]"
    assert actual_data is not None, "response data is empty"
    print("Validating JSONSchema")
    jsonschema.validate(actual_data, users_list_json_schema)


@pytest.mark.parametrize("user_id,expected_status_code", fetching_single_user_test_params)
def test_fetching_single_user(reqres_api_client, user_id, expected_status_code):
    actual_data, actual_status_code = reqres_api_client.get_single_user(user_id)
    assert actual_data
    assert actual_status_code == expected_status_code
    jsonschema.validate(actual_data, single_user_jsonschema)


@pytest.mark.asyncio
@pytest.mark.parametrize("num_of_requests", [100])
async def test_too_many_requests(reqres_api_client, num_of_requests):
    asyncio.Semaphore = 2

    async def make_async_get():
        async with aiohttp.ClientSession() as session:
            async with session.get("https://reqres.in/api/users/1") as response:
                json_data = await response.json()
                status_code = response.status
                return {"data": json_data, "status_code": status_code}

    values = [make_async_get() for _ in range(num_of_requests)]
    results = await asyncio.gather(*values)
    assert all(ele["status_code"] == 404 for ele in results)

    # for request_index in range(num_of_requests):
    #     print(f"making request no. {request_index}")
    #     _, actual_status_code =  reqres_api_client.get_single_user("1")
    #     if actual_status_code == 429:
    #         break
    # assert actual_status_code == 429


async def async_fun():
    async with aiohttp.ClientSession as sessions:
        async with sessions.get("some url") as response:
            await response.json()
