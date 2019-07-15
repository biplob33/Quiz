from django.contrib import admin
from models import qusetion,userprof,sets
class book(admin.ModelAdmin):
    list_display=['username','Year','Roll_No','Score']
class question_or(admin.ModelAdmin):
    list_display=['__str__','no','Year','event','ans']
class sets_or(admin.ModelAdmin):
    list_display=['no','set2_val','set3_val']
admin.site.register(qusetion,question_or)
admin.site.register(userprof,book)
admin.site.register(sets,sets_or)