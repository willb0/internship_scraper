
# internship_scraper

A web app interfacing with a database of internship opportunities scraped using search params

## TODO

- [X] write the python script using selenium/beautifulsoup to identify links
  
  - works using requests and bs4. hits rate limit captcha tho.

- [ ] get SQL db up and running so we can check if links in db etc
- [ ] get basic FastAPI server up that allows a few requests:
  - [ ] in_db GET: takes a list of links and returns the ones not in DB
  - [ ] update_db POST: takes a list of links and puts them in the DB
  - [ ] show_db GET: takes a length n and returns the first n jobs
- [ ] setup cron job or equivalent to run scraping script periodically
