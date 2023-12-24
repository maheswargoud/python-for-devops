import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

# print(response.json())
# print(response.status_code)

complete_details = response.json()
print(compile[0]["id"])