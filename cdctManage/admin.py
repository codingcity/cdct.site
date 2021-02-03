from django.contrib import admin

from .models import Lecture


class LectureAdmin(admin.ModelAdmin):
    search_fields = ['subject']



admin.site.register(Lecture, LectureAdmin)
# Register your models here.
