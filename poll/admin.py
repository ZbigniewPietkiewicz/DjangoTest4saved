from django.contrib import admin

# Register your models here.

from .models import Poll
from .models import Question
from .models import Choice

admin.site.register(Poll)
admin.site.register(Question)
admin.site.register(Choice)