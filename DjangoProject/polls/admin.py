from polls.models import Poll, Choice
from django.contrib import admin

class ChoiceInline(admin.TabularInline):
    model = Choice
    exetra = 3

class PallAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {"fields":["question"]}),
        ("Date information", {"fields":["pub_date"], "classes":["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ("question", "pub_date", "was_published_recently")
    list_filter = ["pub_date"]
    search_fields = ["question"]
    date_hierarchy = "pub_date"

admin.site.register(Poll, PallAdmin)
