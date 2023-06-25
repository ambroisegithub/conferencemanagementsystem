from datetime import date
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    def __str__(self):
        return str(self.name)


class Conference(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    category = models.CharField(max_length=200)
    venue = models.CharField(max_length=100)
    theme = models.CharField(max_length=100)

    def __str__(self):
        return self.title


# def create_dummy_conferences():
#     category = Category.objects.create(name="Category")
#     for i in range(10):
#         Conference.objects.create(
#             title=f"Conference {i}",
#             category=category,
#             date=date(2023, 6, 1),
#             venue="Venue",
#             theme="Theme"
#         )

# create_dummy_conferences()

