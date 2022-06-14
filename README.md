# django-authentification

# objectif du projet

    - créer une authentification (connexion & creation d'utilisateur)

    - utiliser le framework django

    - utiliser le module dotenv pour securiser la secret_key

    - cacher les données sensible de django en mode production (base de données par exemple..)

# install un environnement virtuel

    - pip install virtualenv

    - virtualenv venv

    - source venv/bin/activate

# installer les modules

    - pip install -r requirements.txt 

    ou 

    - pip install django python-dotenv

# installer le projet

    - cd auth 

    - copier le fichier settings_specific.py.sample et le renommer en settings_specific.py

    - créer un fichier .env et générer une SECRET_KEY en utilsant la commande ci-dessous

    python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'

    coller la secret_key générer dans le fichier .env