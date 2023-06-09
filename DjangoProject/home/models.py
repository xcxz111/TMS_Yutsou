from django.db import models


class Feedback(models.Model):
    STATUSES = [
        ("N", "New feedback"),
        ("P", "feedback in process"),
        ("F", "feedback was process")
    ]

    username = models.CharField(max_length=30, verbose_name="Full name")
    email = models.EmailField(verbose_name="user email")
    instagram = models.CharField(max_length=50, verbose_name="user Instagram")
    message = models.TextField(max_length=500, verbose_name="Message")
    status = models.CharField(max_length=1, choices=STATUSES, default="N", verbose_name="feedback status")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created feedback")
    updated = models.DateTimeField(auto_now=True, verbose_name="Last updated")

    class Meta:
        db_table = 'feedback'
        verbose_name = "Feed back"

    def __str__(self):
        return self.username
    
