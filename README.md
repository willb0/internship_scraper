
# internship_scraper

A web app interfacing with a database of internship opportunities scraped using search params

## TODO

- [X] write the python script using selenium/beautifulsoup to identify links
  
  - works using requests and bs4. hits rate limit captcha tho.
  - new implementation with google api need auth tho

- [X] get SQL db up and running so we can check if links in db etc
  - done. used psycog2 for postgres connector 
- [ ] get basic CRUD FastAPI server up that allows a few endpoints:
  - [X] C - POST - Add new job to the database
  - [X] R - GET - Read a job from database by id
  - [ ] U - PATCH - Update job link by id
  - [ ] D - DELETE -  Delete job link by id
- [ ] setup cron job or equivalent to run scraping script periodically
- [ ] dockerize everything
- [ ] build js frontend
- [ ] build full image using docker compose

## SETUP

You will need a google API key attached to a project and a google custom search instance to use the api in gapi_scrape.py. The scrape.py file provides an implementation that doesn't require external auth, but you will be subject to CAPTCHA blocks by google.
<https://stackoverflow.com/questions/37083058/programmatically-searching-google-in-python-using-custom-search>
youll need a creds.json file with custom search id and google api key like this:

```json
[{
    "cse_id":"",
    "api_key": ""
}]
```

once you have that, setup your dev environment:

MacOS/Linux

```bash
python3 -m pip install virtualenv
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

To run the scraper, you can create a test.py file in utils containing:

```python
from gapi_scrape import scrape
# links: list of links of sites you want to scrape
# jobs: list of job titles
# date: jobs since date
scrape(links,jobs,date)

```

To run the web app you need a Postgres table called jobs

```bash
uvicorn main:app --reload
```
