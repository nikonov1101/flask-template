__author__ = 'sshaman'

import os

################
# GLOBAL CONFIG
###############
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

# max content length is 16 megabyte
MAX_CONTENT_LENGTH = 16 * 1024 * 1024

# file upload
ALLOWED_EXTENSIONS = {'png', 'gif', 'jpg', 'jpeg'}
UPLOAD_DIR = os.path.join(BASE_DIR, 'tmp')

###################
# Database config
##################
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASE_DIR, 'migrations')
