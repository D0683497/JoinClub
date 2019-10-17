from django.contrib import admin
from .models import Teacher, Location, Category
from join.models import Position, Degree, College, Department, Lesson

admin.site.register(Position)
admin.site.register(Degree)
admin.site.register(College)
admin.site.register(Department)
admin.site.register(Lesson)
admin.site.register(Teacher)
admin.site.register(Location)
admin.site.register(Category)
