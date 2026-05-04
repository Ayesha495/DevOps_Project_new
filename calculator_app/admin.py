from django.contrib import admin

from .models import Calculator


@admin.register(Calculator)
class CalculatorAdmin(admin.ModelAdmin):
    list_display = ("num1", "operation", "num2", "result", "created_at")
    list_filter = ("operation", "created_at")
    search_fields = ("num1", "num2", "result")
