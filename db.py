
import psycopg2
import os
from urllib.parse import urlparse

#urlparse.uses_netloc.append('postgres')
url = urlparse(os.environ['DATABASE_URL'])

conn = psycopg2.connect("dbname=%s user=%s password=%s host=%s " % (url.path[1:], url.username, url.password, url.hostname))
conn.set_isolation_level(0)
cur = conn.cursor()

queries = ["""
            CREATE TABLE elevation (e_id INTEGER, e_name VARCHAR(255), e_elevation INTEGER)
            """,
           """
            CREATE TABLE run (r_id INTEGER, r_name VARCHAR(255), r_result VARCHAR(20))
           """
          ]
for q in queries
  cur.execute(query)

conn.commit()  
