from psycopg2 import connect
from psycopg2.extras import execute_values
from gapi_scrape import scrape

# init db
con = connect(database="postgres", user='postgres',
                       password='database', host='127.0.0.1', port='5432')
cur = con.cursor()
#cur.execute('DROP TABLE jobs;')

# get links to jobs
links = ['lever.co']
jobs = ['data engineer intern']
date_posted = '2021-10-08'
num_jobs = 5
jobs = scrape(links, jobs, date_posted)
print(jobs)

# create table
create_query = """
CREATE TABLE jobs
(job_id SERIAL PRIMARY KEY,
job_link TEXT NOT NULL);"""
cur.execute(create_query)

# insert jobs
insert_query = """
INSERT INTO jobs(job_link) VALUES(%s);
"""
for job in jobs:
    cur.execute(insert_query,(job,))
    con.commit()
# try to select jobs to see if it works
select_query = """
SELECT job_id,job_link from jobs;
"""
cur.execute(select_query)
print(cur.fetchall())




