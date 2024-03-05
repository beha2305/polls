from django.contrib import admin
from .models import Questions, Answers

question = admin.site.register(Questions)
answer = admin.site.register(Answers)
