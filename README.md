## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

### Deploiement

Il est nécessaire d’installer docker, avoir un compte DockerHub, Heroku, Sentry, et CircleCI.

Heroku :

-	Créer une nouvelle application 
-	Dans « Account settings », récupérer ou générer votre « API key »
-	Garder cette valeur car on en aura besoin plus tard

Sentry :

-	Sur le site, cliquer sur `Projects` , `Create Project`  ensuite  `Django`
-	Créer votre projet en appuyant sur `Create Project`
-	Récupérer la valeur dans `dsn=` et garder la pour plus tard  

CircleCI :

1. Sur le site CircleCI, se rendre sur `Projects` et cliquer sur `Set Up Project` avec le projet concerné
2. Choisissez la deuxième option et entrez `master` si besoin comme nom de branche puis `Let’s go`
3. Cliquer sur `Projects Settings` , ensuite `Environment Variables` et pour terminer `Add Environment Varibale` 
4. Ajouter les variables d’environnement suivantes et compléter les :
  -	`ALLOWED_HOSTS` : url de votre application Heroku ( ex : app-name.herokuapp.com)
  -	`DEBUG` : False
  -	`DOCKER_HUB_PASSWORD` : mot de passe votre compte DockerHub
  -	`DOCKER_HUB_USERNAME` : pseudo votre compte DockerHub
  -	`HEROKU_API_KEY` : valeur récupérer dans la partie Heroku
  -	`HEROKU_APP_NAME` : Nom de l’application créé préalablement
  -	`HEROKU_LOGIN` : email de votre compte Heroku
  -	`SECRET_KEY` : créer votre clé secrète ou générer la [ici](https://djecrety.ir/)
  -	`SENTRY_DSN` : valeur récupérer dans la partie Sentry
5. Relancer le workflow 

### Docker
Il faut préalablement installer Docker.

1. Lancer une invite de commande en tant qu’administateur
2. Remplacer les variables `container_name`, `docker_hub_username`, `heroku_app_name` et `tags` qui correspond aux tags de votre image crée ( à récupérer dans `Images` puis `Remote repositories`) dans la commande ci-dessous
3. Exécuter la commande suivante : docker run --name `container_name` -dp 80:8000/tcp `docker_hub_username`/`heroku_app_name`:`tags` 
4. Aller sur `http://localhost/`
