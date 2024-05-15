from django.db import models
from users.models import User  # Assuming you have a User model in your users app

class Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_content = models.TextField()
    heart_rate = models.FloatField()
    blood_pressure_systolic = models.FloatField()
    blood_pressure_diastolic = models.FloatField()
    body_temperature = models.FloatField()
    blood_oxygen_saturation = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Therapy Session on {self.date.strftime('%Y-%m-%d %H:%M:%S')}"


class DoctorFollowing(models.Model):
    doctor = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.doctor.username} follows {self.user.username}"