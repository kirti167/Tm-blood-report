from django.contrib import admin
from .models import Document, Tweet,Patient,TestResult
# Register your models here.
admin.site.register(Tweet)
admin.site.register(Patient)
admin.site.register(Document)
