from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

class User(AbstractUser):
    pass

class BaseModel(models.Model):
    class Meta:
        abstract = True
    create_date = models.DateField(auto_now_add=True, null= True)
    update_date = models.DateField(auto_now=True,null= True)
    active = models.BooleanField(default=True)

class Category(BaseModel):
    name = models.CharField(max_length=50, null= False)

    def __str__(self):
        return self.name


class ItemBase(models.Model):
    class Meta:
        abstract = True
    subject = models.CharField(max_length=250, null =False)

    def __str__(self):
        return self.subject
class Course(BaseModel,ItemBase):

    class Meta:
        unique_together = ('subject','category')
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='courses/%Y/%m')
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    tag = models.ManyToManyField('Tag')

class Lesson(BaseModel,ItemBase):
    class Meta:
        unique_together = ('subject','course')
    content = RichTextField()
    image = models.ImageField(upload_to='lessons/%Y/%m')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    tag = models.ManyToManyField('Tag')

class Tag(BaseModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

