from django.db import models

class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        abstract = True


class Contact(TimestampedModel):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=60)
    phone = models.CharField(max_length=15, blank=True, null=True)
    message = models.TextField()


    def __str__(self):
        return self.message