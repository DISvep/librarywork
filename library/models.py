from django.db import models


# Create your models here.
class LibraryBook(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    available = models.BooleanField(default=False)

    class Meta:
        ordering = ['author']
        indexes = [
            models.Index(fields=['isbn'], name='isbn_idx'),
        ]

    def __str__(self):
        return f"{self.author} - {self.title}"
