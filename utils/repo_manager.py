import requests
from secret import GITHUB_TOKEN

USERNAME = "Tkspt"

def create_github_repo(repo_name):
    url = f"https://api.github.com/user/repos"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "name": repo_name,
        "private": False
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print(f"Dépôt '{repo_name}' créé avec succès.")
        return response.json()
    else:
        print(f"Erreur lors de la création du dépôt : {response.json()}")
        return None

def create_github_issue(repo_name, issue_title, issue_body):
    url = f"https://api.github.com/repos/{USERNAME}/{repo_name}/issues"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "title": issue_title,
        "body": issue_body
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print(f"Issue '{issue_title}' créée avec succès.")
    else:
        print(f"Erreur lors de la création de l'issue : {response.json()}")