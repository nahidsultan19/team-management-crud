from django.db import models

Genre = (
    ('Science', 'Science'),
    ('History', 'History'),
)


class Book(models.Model):
    name = models.CharField(max_length=50)
    book_name = models.CharField(max_length=100)
    pub_date = models.DateField(auto_now_add=True, blank=True, null=True)
    genre = models.CharField(choices=Genre, max_length=10)

    def __str__(self):
        return self.name
