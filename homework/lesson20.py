import requests

BASE_URL = "https://petstore.swagger.io/v2"
PET_ID = 123

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}

#POST
data_for_post = {
    "id": PET_ID,
    "category": {"id": 1, "name": "МЕДОЕДЫ"},
    "name": "Стасик",
    "photoUrls": ["string"],
    "tags": [{"id": 1, "name": "КЕН"}],
    "status": "available",
}

response_post = requests.post(
    f"{BASE_URL}/pet",
    json=data_for_post,
    headers=headers,
)

print("POST status code:", response_post.status_code)

if response_post.status_code == 200:
    print("POST response body:", response_post.json())
else:
    print("POST failed")

#GET
response_get = requests.get(
    f"{BASE_URL}/pet/{PET_ID}",
    headers={"accept": "application/json"},
)

print("GET status code:", response_get.status_code)

if response_get.status_code == 200:
    print("GET response body:", response_get.json())
else:
    print("GET failed")

#PUT
data_for_put = {
    "id": PET_ID,
    "category": {"id": 1, "name": "МЕДОЕДЫ"},
    "name": "Стасик-Обновлённый",
    "photoUrls": ["string"],
    "tags": [{"id": 2, "name": "ХИЩНИК"}],
    "status": "available",
}

response_put = requests.put(
    f"{BASE_URL}/pet",
    json=data_for_put,
    headers=headers,
)

print("PUT status code:", response_put.status_code)

if response_put.status_code == 200:
    print("PUT response body:", response_put.json())
else:
    print("PUT failed")

#DELETE
response_delete = requests.delete(
    f"{BASE_URL}/pet/{PET_ID}",
    headers={"accept": "application/json"},
)

print("DELETE status code:", response_delete.status_code)

if response_delete.status_code == 200:
    print("DELETE response body:", response_delete.json())
else:
    print("DELETE failed")
