# from django.contrib import admin
# from .models import Course, Lesson

# class LessonInline(admin.TabularInline):
#     model = Lesson
#     extra = 1

# @admin.register(Course)
# class CourseAdmin(admin.ModelAdmin):
#     list_display = ['title']
#     inlines = [LessonInline]

# @admin.register(Lesson)
# class LessonAdmin(admin.ModelAdmin):
#     list_display = ['title', 'course', 'is_premium']
