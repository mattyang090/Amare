from __future__ import unicode_literals
from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        matching_user = User.objects.filter(email = postData['email'])
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Email must be valid"
        elif len(matching_user) > 0:
            errors['email'] = "Email taken"
        if len(postData['password']) < 8:
            errors['password'] = "Password must be more than 8 characters"
        if postData['password'] != postData['c_password']:
            errors['c_pass'] = "Passwords must match"
        return errors
    
    def login_validator(self, postData):
        errors = {}
        matching_user = User.objects.filter(email = postData['email'])
        if len(matching_user) == 0:
            errors['invalid'] = "Email not found"
        elif postData['password'] == "":
            errors['invalid'] = "Please enter a password"
        elif not bcrypt.checkpw(postData['password'].encode(), matching_user[0].password.encode()):
            errors['invalid'] = "Failed password"
        return errors
    
class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255, null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
