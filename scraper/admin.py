from django import forms
from django.contrib import admin, messages
from django.db import models
from import_export.admin import ImportExportModelAdmin

from scraper.models import Keyword
from scraper.resources import KeywordResource
from scraper.tasks import scrape_task


@admin.register(Keyword)
class KeywordAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    '''Admin integration for keyword.'''

    resource_class = KeywordResource
    formfield_overrides = {models.TextField: {'widget': forms.TextInput}}
    search_fields = ('keyword', )
    list_filter = ('category', 'scraped')
    list_display = ('keyword', 'category', 'scraped')
    actions = ('scrape_action', )

    def get_message(self, task_name, count):
        if count == 1:
            return 'Delayed {} for 1 keyword.'.format(task_name)
        return 'Delayed {} for {} keywords.'.format(task_name, count)

    def scrape_action(self, request, queryset):
        '''Admin action for scraping pinterest keywords suggestions.'''
        for keyword in queryset:
            scrape_task.delay(keyword)
        self.message_user(
            request,
            self.get_message('scrape_task', queryset.count()),
            level=messages.SUCCESS
        )

    scrape_action.short_description = 'Scrape task for selected keywords'
