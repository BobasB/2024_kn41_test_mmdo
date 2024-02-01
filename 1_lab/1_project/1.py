import requests
r = requests.get('https://google.com')
print(f"Програма запустилась, відповідь від сайту буде: {r.status_code}")
