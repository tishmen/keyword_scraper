from import_export import resources

from scraper.models import Keyword


class CustomResource(resources.ModelResource):

    def dehydrate_id(self, keyword):
        '''Dehydrate id value on export.'''
        return ''


class KeywordResource(CustomResource):

    class Meta:
        model = Keyword
        exclude = ('scraped', 'added_at', )
