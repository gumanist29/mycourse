from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=150, null=True)

    class Meta:
        verbose_name = 'Категория'

    def __str__(self):
        return self.name


class Course(models.Model):
    ids = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    category = models.ForeignKey(Category, related_name='courses', on_delete=models.CASCADE)
    logo = models.CharField(max_length=150)

    def __str__(self):
        return self.ids


class Branch(models.Model):
    address = models.CharField(max_length=200)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    course = models.ForeignKey(Course, related_name='branches', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Отрасли'

    def __str__(self):
        return self.address

contact_type = (
        ('Phone', 'PHONE'),
        ('Facebook', 'FACEBOOK'),
        ('Email', 'EMAIL'),
    )
class Contact(models.Model):
    type = models.CharField(max_length=20,choices=contact_type, default='Phone')
    value = models.CharField(max_length=250)
    course = models.ForeignKey(Course, related_name='contacts', on_delete=models.CASCADE)

    def __str__(self):
        return self.value

