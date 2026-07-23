import requests
import json

api = "http://localhost:3000/mobiles"

send_data = {
  "id":20,
  "brand": "IQOO",
  "model": "z7 pro",
  "price": 39999
}

try:
  # Use `json=` with a Python object so requests sets Content-Type correctly
  res = requests.post(api, json=send_data, timeout=10)
  print(res.status_code)
  try:
    print(res.json())
  except ValueError:
    print(res.text)
except requests.exceptions.RequestException as e:
  print("Request failed:", e)
