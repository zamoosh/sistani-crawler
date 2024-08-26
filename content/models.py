from django.db import models


class Content(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    body = models.TextField(null=True, blank=True)
    foot_note = models.TextField(null=True, blank=True)
