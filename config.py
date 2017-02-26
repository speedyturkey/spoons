import os
# Initial values copied from microblog sample application.

# WTF_CSRF_ENABLED = True
# SECRET_KEY = 'you-will-never-guess'
#
basedir = os.path.abspath(os.path.dirname(__file__))
#
# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
# SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')


mysql = {'user': 'root',
        'password': 'qiq7!grCzJ5H',
        'endpoint': 'flasktest.crczz2ty7t4q.us-west-2.rds.amazonaws.com',
        'port': 3306,
        'database': 'flaskdb'
        }

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{endpoint}:{port}/{database}'.format(**mysql)
