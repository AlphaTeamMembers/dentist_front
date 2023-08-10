from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, blank=True, null=True)
    short_intro = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    instagram = models.CharField(max_length=200, blank=True, null=True)
    facebook = models.CharField(max_length=200, blank=True, null=True)
    tvitter = models.CharField(max_length=200, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(default='dafault.jpeg', blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class About(models.Model):
    image = models.ImageField(upload_to='about')
    title = models.CharField(max_length=30)
    description = models.TextField()
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'About'


class SendAppointment(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=20)
    time = models.DateTimeField(unique=True)
    message = models.TextField(blank=True, null=True)
    crated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_solved = models.BooleanField(default=False)

    def __str__(self):
        return self.subject


class Blog(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='blog')
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_solved = models.BooleanField(default=False)

    def __str__(self):
        return self.name
