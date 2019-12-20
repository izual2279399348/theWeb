import os

DEBUG = True
WTF_CSRF_ENABLED = False
WTF_CSRF_SECRET_KEY = 'a random string'
SECRET_KEY = 'my precious'
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'database.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASE_DIR, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True
HOST = 'localhost'
PORT = int(os.environ.get('PORT', 5000))
