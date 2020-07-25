from django.contrib import admin
from . import models


@admin.register(models.Post)
class Post(admin.ModelAdmin):

    """ Post Model Definition """

    pass
