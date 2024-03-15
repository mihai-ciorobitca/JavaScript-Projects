import requests

url = "https://apps.growmeorganic.com/api-product/incoming-webhook/extract-emails-from-urls"
data = {
    "api_key": "your_api_key",
    "url": "https://extractemails.com"
}

headers = {
    "Content-Type": "application/json",
}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    print("Request successful. Response:")
    print(response.json())
else:
    print(f"Request failed with status code {response.status_code}. Response:")
    print(response.text)
