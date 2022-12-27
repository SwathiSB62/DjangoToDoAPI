from django.db import models
from django.contrib.auth import models as auth_models

class UserManager(auth_models.BaseUserManager):
    def create_user(self, email: str, password: str= None) -> "User":
        if not email:
            raise ValueError("User must have an email address") 
        user=self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user

class User(auth_models.AbstractUser):
    email = models.EmailField(verbose_name="Email",max_length=255,unique=True)
    password = models.CharField(max_length=255)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)
    username = None

    object = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

class Todo(models.Model):
    class StatusChoices(models.TextChoices):
        notstarted = "NotStarted"
        ongoing = "OnGoing"
        completed = "Completed"
    name = models.CharField(max_length=500, null=False, blank=False)
    description = models.TextField(blank=True,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    updated_timestamp = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=14, choices=StatusChoices.choices, default=StatusChoices.notstarted,)
    userid = models.PositiveIntegerField()

    def __str__(self):
        return self.name