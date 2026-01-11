import requests

# Создание вызова API и сохранение ответа.
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Преобразование объекта ответа в словарь.
response_dict: dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")

# Анализ информации о репозиториях.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Прочитаем значения некоторых ключей:
print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Description: {repo_dict['description']}")
    print()
