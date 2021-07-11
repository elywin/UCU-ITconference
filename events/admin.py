from django.contrib import admin
from .models import Guest, AboutUs, OurGoal, FAQs, EventTitles, Answer


# Register your models here.
admin.site.register(Guest)
admin.site.register(AboutUs)
admin.site.register(OurGoal)
admin.site.register(FAQs)
admin.site.register(EventTitles)
admin.site.register(Answer)