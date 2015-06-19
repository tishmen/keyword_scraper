import logging
import traceback

from celery import shared_task

from scraper.scraper import Scraper

log = logging.getLogger('keyword_scraper')


@shared_task(bind=True)
def scrape_task(self, keyword):
    '''Celery task for scraping pinterest keyword suggestions.'''
    try:
        Scraper()(keyword)
    except Exception:
        log.error('Traceback: %s', traceback.format_exc())
        raise
