from django.contrib import admin
from .models import Course, Module, Section, Video, Assignment, Question,Answer, Test, TestQuestion

admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Section)
admin.site.register(Video)
admin.site.register(Assignment)
admin.site.register(Question)
admin.site.register(Test)
admin.site.register(TestQuestion)
admin.site.register(Answer)