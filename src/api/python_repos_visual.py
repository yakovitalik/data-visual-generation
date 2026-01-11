import requests
import plotly.express as px

# Создание вызова API и сохранение ответа.
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Обработка результатов
response_dict: dict = r.json()
print(f"Complete results: {not response_dict['incomplete_results']}")

# Обработка информации о репозиториях.
repo_dicts = response_dict['items']
repo_names, stars = [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# Создание визуализации
fig = px.bar(x=repo_names, y=stars)
fig.show()
