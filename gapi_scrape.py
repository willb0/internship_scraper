from googleapiclient.discovery import build
import json
num_page = 5

creds = json.load(open('creds.json'))[0]
cse_id = creds['cse_id']
api_key = creds['api_key']

# https://stackoverflow.com/questions/37083058/programmatically-searching-google-in-python-using-custom-search
def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

def scrape(links:list,jobs:list,date_posted:str)-> list:

    ## initialize requests session 
    data = []
    #s = requests.session()
    # join our links if theres more than 1
    link = ' OR '.join(links) if len(links) > 1 else links
    # iterate through jobs and search them 
    for job in jobs:
        url = 'https://www.google.com/search?q='
        kwds = '+'.join(job.split())
        query = f'after:{date_posted} site {link} {kwds}'
        links = [result['link'] for result in google_search(query,api_key,cse_id)]
        data.extend(links)
    return list(set(data))

'''
links = ['jobs.lever.co']
jobs = ['data engineer intern']
date_posted = '2021-10-03'
num_jobs = 5
print(scrape(links, jobs, date_posted))
'''