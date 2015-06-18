import logging
import json
import re

import requests

from scraper.models import Keyword

log = logging.getLogger('keyword_scraper')


class Scraper(object):

    '''Scrape pinterest keyword suggestions and generate new ones.'''

    def get_data(self, url):
        '''Return json from page source. Pinterest specific.'''
        response = requests.get(url)
        result = re.search('P.start.start\((.*)\);', response.text)
        data = json.loads(result.group(1))
        log.debug('Got json data from %s.', url)
        return data

    def generate_keyword(self, keyword, term, position):
        '''Return 'term keyword' if position is 0 else 'keyword term'.'''
        if position == 0:
            return '{} {}'.format(term, keyword)
        return '{} {}'.format(keyword, term)

    def save_keywords(self, keyword, json):
        '''Get and save generated keyword objects.'''
        for result in json['resourceDataCache'][0]['data']['guides']:
            Keyword.objects.create(
                keyword=self.generate_keyword(
                    keyword, result['term'], result['position']
                ),
                category=keyword.category,
                scraped=True
            )

    def __call__(self, keyword):
        '''Run code for Scraper.'''
        data = self.get_data(keyword.url())
        self.save_keywords(keyword, data)
