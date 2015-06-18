from import_export import resources

from scraper.models import Keyword


class KeywordResource(resources.ModelResource):

    '''Resource class for keyword.'''

    class Meta:
        model = Keyword
        exclude = ('scraped', 'added_at', )

    def dehydrate_id(self, keyword):
        '''Remove id values while exporting.'''
        return ''
