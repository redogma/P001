import psycopg2
import os
from urllib.parse import urlparse
from urllib.request import urlopen
from bs4 import BeautifulSoup

def connect():
    url = urlparse(os.environ['DATABASE_URL'])


    conn = psycopg2.connect("dbname=%s user=%s password=%s host=%s " % (url.path[1:], url.username, url.password, url.hostname))
    conn.set_isolation_level(0)
    cur = conn.cursor()

    return conn, cur

def save_elevations(value):
    print('** Saving elevations to reference table')	
    conn, cur = connect()
    sql = 'INSERT INTO reference (ref_key, ref value) values (\'elevations\',' + str(value) + '\')'
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()
    print('** Closing connection')


def get_elevations():
	url = 'https://jegmar.com/stats-hq/fastest-races/parkrun'
	print('** Getting external data')
	html = urlopen(url)
	
	soup = BeautifulSoup(html, 'html5lib')
	
	tr = soup.find_all('tr')
	
	runs =[]
	for row in tr: #[0:10]:
		line = ''
		for cell in row.find_all(['th','td'],class_=['column-1','column-2', 'column-4']):
			line = line + ',' + cell.get_text().strip()
		elements = line[1:].split(',')
		runs.append ({'pos': elements[0], 'run': elements[1], 'elevation': elements[2]})

	return runs[1:]

def create_tables():
    conn, cur = connect()
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
    cur.close()
    conn.close()
    print('** Closing connection')
            
if __name__ == '__main__':
    pass            
