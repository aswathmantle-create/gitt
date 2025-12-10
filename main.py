print("Hello from Codespaces!")

# tiny example: fetch a webpage
import requests

url = "https://example.com"
response = requests.get(url)
print("Status code:", response.status_code)
git add .
git commit -m "Add first python script"
git push
