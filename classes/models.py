# models.py
from django.db import models

class contactus(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    comment = models.TextField()

    def __str__(self):
        return f"{self.firstname} {self.lastname} - {self.email}"

    class meta:
        db="classes_contactus"


# models.py
from django.contrib.auth.models import User

# from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=100)
    pdf_link = models.URLField()
    video_link = models.URLField()

    def _str_(self):
        return self.title


class CourseRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'course')


class OnlineClass(models.Model):
    title = models.CharField(max_length=100, unique=True)
    zoom_link = models.URLField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.title}"

    class Meta:
        db_table = "classes_onlineclass"

class OnlineClassRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    online_class = models.ForeignKey(OnlineClass, on_delete=models.CASCADE)
    registered_on = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.user.username} - {self.online_class.title}"


# project/models.py
from django.db import models

class Faculty(models.Model):
    name = models.CharField(max_length=100)  # Optional photo field
    description = models.TextField()
    course = models.CharField(max_length=50)  # Which course this faculty belongs to (e.g., Japanese, French)

    def __str__(self):
        return self.name


from django.db import models

class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


