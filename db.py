import psycopg2
import os
from urllib.parse import urlparse

'urlparse.uses_netloc.append('postgres')
url = urlparse.urlparse(os.environ['DATABASE_URL'])

conn = psycopg2.connect("dbname=%s user=%s password=%s host=%s " % (url.path[1:], url.username, url.password, url.hostname))
cur = conn.cursor()

query = "SELECT 1"
cur.execute(query)
