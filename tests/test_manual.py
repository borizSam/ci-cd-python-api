import requests

r = requests.get("http://localhost:8000/")
print(r.status_code, r.json())

r = requests.get("http://localhost:8000/health")
print(r.status_code, r.json())