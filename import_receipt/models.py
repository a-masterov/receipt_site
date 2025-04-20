from django.db import models

class SiteSetting(models.Model):
    google_login_enabled = models.BooleanField(default=True)

