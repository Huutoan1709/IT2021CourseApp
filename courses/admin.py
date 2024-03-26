from django.contrib import admin
from .models import Category, Course, Lesson, Tag
from django.utils.html import mark_safe
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']
    search_fields = ['name']
    list_filter = ['id', 'name']


class CourseAdmin(admin.ModelAdmin):
    list_display = ['pk', 'subject', 'description']
    search_fields = ['subject']
    readonly_fields = ['img']

    def img(self, course):
        if course:
            return mark_safe(
                '<img src="/static/{url}" width="120"/>'\
                .format(url=course.image.name)
            )


class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)

    class Meta:
        model = Lesson
        fields = '__all__'


class LessonAdmin(admin.ModelAdmin):
    list_display =['id', 'subject', 'create_date', 'active']
    form = LessonForm


admin.site.register(Category, CategoryAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Tag)


