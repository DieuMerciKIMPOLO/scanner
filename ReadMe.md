## Source: https://www.django-rest-framework.org/tutorial/quickstart/

## Installation de l'environnement virtuel
python3 -m venv env
## Activation de l'environnement virtuel
En etant dans le meme dossier de creation executer l'instruction suivante:
source env/bin/activate
## Lien d'acces interface d'admin:
http://127.0.0.1:8000/admin/login/?next=/admin/
## Migration 
python manage.py migrate
## Creation du super-user:
python manage.py createsuperuser --email thierno@scanproject.com --username thierno
Passwor: thierno__123

## Generate requirements:
pip freeze > requirements.txt

## Install requirements
pip install -r requirements.txt


