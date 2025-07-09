from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=11)
    password = models.CharField(max_length=20)
    code = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    

class Role(models.Model):
    role_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_role')
    created_at = models.DateTimeField(auto_now_add=True)
    
