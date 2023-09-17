from django.db import models
import secrets
import string  # Import the 'string' module

class BoatRegistration(models.Model):
    bix_id = models.CharField(max_length=50)
    license_number = models.CharField(max_length=50)
    aadhar_number = models.CharField(max_length=12)
    duration = models.CharField(max_length=50)
    boat_type = models.CharField(max_length=50)
    token = models.CharField(max_length=22, blank=True)

    def __str__(self):
        return self.bix_id

    class Meta:
        app_label = 'bix' 

    def save(self, *args, **kwargs):
        if not self.token:
            # Generate a random URL-safe token
            characters = string.ascii_letters + string.digits + "-_"
            self.token = ''.join(secrets.choice(characters) for _ in range(22))
        super().save(*args, **kwargs)  # Call the parent class's save method
