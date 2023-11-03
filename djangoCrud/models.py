from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    message = models.TextField()
    # contact_at=models.DateTimeField(auto_now_add=True)