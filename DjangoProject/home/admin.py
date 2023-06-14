from django.contrib import admin
from home.models import Feedback


class AdminFeedback(admin.ModelAdmin):
    list_display = ("username", "status", "updated")


admin.site.register(Feedback, AdminFeedback)