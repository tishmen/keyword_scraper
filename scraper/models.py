from django.db import models

CATEGORIES = [
    'animals', 'architecture', 'art', 'cars_motorcycles', 'celebrities',
    'design', 'diy_crafts', 'education', 'film_music_books', 'food_drink',
    'gardening', 'geek', 'hair_beauty', 'health_fitness', 'history',
    'holidays_events', 'home_decor', 'humor', 'illustrations_posters', 'kids',
    'mens_fashion', 'outdoors', 'photography', 'products', 'quotes',
    'science_nature', 'sports', 'tattoos', 'technology', 'travel', 'weddings',
    'womens_fashion', 'other'
]


class Keyword(models.Model):

    class Meta:
        unique_together = ('keyword', 'category')

    keyword = models.TextField()
    category = models.CharField(
        max_length=21,
        choices=((category, category) for category in CATEGORIES)
    )
    scraped = models.BooleanField(default=False)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.keyword

    def url(self):
        '''Return pinterest keyword search query.'''
        return 'https://www.pinterest.com/search/?q={}'.format(
            self.keyword.replace(' ', '+')
        )
