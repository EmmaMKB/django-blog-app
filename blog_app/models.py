from django.db import models
from django.utils import timezone
import uuid
# Create your models here.


class BlogPost(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, default="")
    content = models.CharField(max_length=4096, default="<h1>No content Yet</h1>")
    date_posted = models.DateTimeField(default=timezone.now)
