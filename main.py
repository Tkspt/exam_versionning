from utils.repo_manager import create_github_repo, create_github_issue

REPO_NAME = "exam_versionning"

# Créer un dépôt
repo_info = create_github_repo(REPO_NAME)

# Si le dépôt a été créé avec succès, ajouter deux issues
if repo_info:
    create_github_issue(REPO_NAME, "Première issue", "Ceci est la première issue.")
    create_github_issue(REPO_NAME, "Deuxième issue", "Ceci est la deuxième issue.")