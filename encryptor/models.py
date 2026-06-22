from django.db import models

class Password(models.Model):
    account = models.CharField(max_length=30 ,null=True)
    encryption = models.TextField()

    def __str__(self):
        return self.account