import requests
import os
print(f"Ми запускаємось у середовищі {os.environ['ENV_NAME']} для проекту {os.environ['PROJECT_NAME']}")

response = requests.get('https://httpbin.org/')

print(f"Відповідь від URL {response.url} буде {response.status_code}")
print(f"Кількість стрічок які повернулись у запиті: {len(list(response.iter_lines()))}")
    