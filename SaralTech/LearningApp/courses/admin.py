from django.contrib import admin
from .models import Course, Module, Section, Video, Assignment, Question, Test, TestQuestion

admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Section)
admin.site.register(Video)
admin.site.register(Assignment)
admin.site.register(Question)
admin.site.register(Test)
admin.site.register(TestQuestion)
