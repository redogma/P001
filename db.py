import psycopg2
import os
from urllib.parse import urlparse

#urlparse.uses_netloc.append('postgres')
url = urlparse(os.environ['DATABASE_URL'])

conn = psycopg2.connect("dbname=%s user=%s password=%s host=%s " % (url.path[1:], url.username, url.password, url.hostname))
conn.set_isolation_level(0)
cur = conn.cursor()

queries = ["""
            CREATE TABLE elevation (e_id INTEGER PRIMARY KEY, e_pos INTEGER, e_name VARCHAR(100), e_elevation INTEGER)
            """,
           """
            CREATE TABLE run (r_id INTEGER, r_name VARCHAR(255), r_result VARCHAR(20))
           """,
           """
             CREATE TABLE reference (ref_id SERIAL PRIMARY KEY, 
                                     ref_key VARCHAR(20), 
                                     ref_value BYTEA, 
                                     ref_modified_date VARCHAR(30))
           """,
           """
              INSERT INTO reference (ref_key, ref_value) VALUES (\'NAME\', \'P001\')
           """,
           """
              INSERT INTO elevation VALUES (1,1,\'Test\', 100)
           """,
           """
              INSERT INTO run VALUES (1,\'Test\', \'30:01\')
           """
          ]
for q in queries:
  print('** Starting: %s' % (q,))
  cur.execute(q)

print('** Finished running queries')
conn.commit()  
