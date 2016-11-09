from django.contrib import admin

from .models import Post, PolicePost, ObjectPost
# Register your models here.
admin.site.register(Post)

admin.site.register(PolicePost)
admin.site.register(ObjectPost)