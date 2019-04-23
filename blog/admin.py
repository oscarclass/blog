from django.contrib import admin
from .models import Category,FreePoster,Post,Comment,StablePage

admin.site.register(Category)
admin.site.register(FreePoster)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(StablePage)