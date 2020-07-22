from django.db import models
from datetime import datetime

class Manager(models.Manager):
    def validate(self, formData):
        errors = {}
        if len(formData['name']) < 5:
            errors["name"] = "Show title should be at least 5 characters"
        if len(formData['desc']) < 10:
            errors['desc'] = "Description should be at least 10 characters"
        return errors

class Courses(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = Manager()