from django.contrib import admin
from .models import *
# Register your models here.

class AboutMw(admin.ModelAdmin):
    list_display = ['id','information','projects','experience','happy_clients','customers']
admin.site.register(AboutMe,AboutMw)

admin.site.register(Skill)
admin.site.register(TimeLine)
admin.site.register(Portfolio)
admin.site.register(Blog)
admin.site.register(Contact)
admin.site.register(Feedback)
admin.site.register(BotUser)