
# internship_scraper

A web app interfacing with a database of internship opportunities scraped using search params

## TODO

- [X] write the python script using selenium/beautifulsoup to identify links
  
  - works using requests and bs4. hits rate limit captcha tho.
  - need a creds.json file with custom search id and google api key like this:

  ```json
  [{
    "cse_id":"",
    "api_key": ""
  }]
  ```

- [X] get SQL db up and running so we can check if links in db etc
  - done. used psycog2 for postgres connector 
- [ ] get basic CRUD FastAPI server up that allows a few endpoints:
  - [X] C - POST - Add new job to the database
  - [X] R - GET - Read a job from database by id
  - [ ] U - PATCH - Update job link by id
  - [ ] D - DELETE -  Delete job link by id
- [ ] setup cron job or equivalent to run scraping script periodically
