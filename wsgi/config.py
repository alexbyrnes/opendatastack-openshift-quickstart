import os

DB_HOST = os.environ.get('OPENSHIFT_POSTGRESQL_DB_HOST')
DB_PORT = os.environ.get('OPENSHIFT_POSTGRESQL_DB_PORT')
APP_NAME = os.environ.get('OPENSHIFT_APP_NAME')
DB_USER = os.environ.get('OPENSHIFT_POSTGRESQL_DB_USERNAME')
DB_PASSWORD = os.environ.get('OPENSHIFT_POSTGRESQL_DB_PASSWORD')

DEBUG = True 
SERVER_NAME = '127.0.0.1'
SERVER_PORT = 80 
DB_CONNECTION = "host='{0}' port='{1}' dbname='{2}' user='{3}' password='{4}'".format(DB_HOST, DB_PORT, APP_NAME, DB_USER, DB_PASSWORD)

METADATA_DB = 'metadb'
METADATA_COLLECTION = 'metadata'

