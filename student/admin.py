from django.contrib import admin
from .models import Student



@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'age', 'is_active')
    list_filter = ('is_active', 'age')
    search_fields = ('first_name', 'last_name')
    ordering = ('-id',)
