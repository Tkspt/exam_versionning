# Git Worktree, c'est quoi ?
C'est une fonctionnalité de Git qui permet de travailler avec plusieurs répertoires de travail liés à un même dépôt Git. Il vous permet d'avoir plusieurs copies d'un même dépôt sur notre machine pysique, chacune pointant vers une branche ou un commit différent. Il permet de faciliter le travail sur différentes branches en parallèle sans avoir à effectuer de git checkout à chaque fois que l'on change de branche.

# Comment créer un nouveau Worktree
Pour créer un Worktree, il suffit de se positionner dans le dépôt Git (cd /chemin/vers/mon/depot)
Et ensuite exécuter la commande (git worktree add /chemin/vers/nouveau-worktree feature-branch)
Ainsi, on vient de créer un nouveau worktree qui pointe sur la branche feature-branch


# Exemple Pratique
Pour exemple on peut prendre le cas d'un hotfix imminent, alors qu'on traivailler sur une autre branche, on peut juste créer un nouveau worktree pour gérer le hotfix sans pour autant qu'il géne le travail que l'on effectue dans notre branche actuelle