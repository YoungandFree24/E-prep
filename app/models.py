

# Create your models here.
from django.db import models
import re

# Create your models here.

class UserManager(models.Manager):
    def reg_validator(self, postData):
        errors={}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len (postData['first_name']) < 3:
            errors['first_name'] = "first name must be at least 3 characters." 
        if len (postData['last_name']) < 3:
            errors['last_name'] = "Last name must be at least 3 characters." 
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid Email"
        # test whether a field matches the pattern 
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters."
        if postData['password'] != postData['confirm_pw']:
            errors['confirm_pw'] = "Passwords don't match!!!!"
        return errors

    def login_validator(self,postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['login_email']):
            errors['login_email'] = "Invalid Email/Password"
        if len(postData['login_password']) < 8:
            errors['login'] = "Invalid Email/Password"
        return errors

    def edit_validator(self, postData):
        errors={}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['edit_login_email']):
            errors['edit_email'] = "Invalid Email/Password/everything_else"
        if len (postData['edit_first_name']) < 3:
            errors['first_name'] = "first name must be at least 3 characters." 
        if len (postData['edit_last_name']) < 3:
            errors['edit_last_name'] = "Last name must be at least 3 characters." 
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email= models.CharField(max_length=45)
    password= models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class QuoteManager(models.Manager):
    def Quote_validatior(self, postData):
        errors={}
        if len(postData['author']) < 3:
            errors['author'] = "Author name must be at least 3 chracters"
        if len(postData['quote_desc']) < 10:
            errors['quote_desc'] = "Quote name must be at least 10 chracters"
        return errors

class Quote(models.Model):
    author = models.CharField(max_length=45)
    quote_desc = models.CharField(max_length=45)
    # one to many relationship below
    user = models.ForeignKey(User, related_name="quotes", on_delete = models.CASCADE)
    # many to many relationship below
    likes=models.ManyToManyField(User, related_name="liked_by")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = QuoteManager()