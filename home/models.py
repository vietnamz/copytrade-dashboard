from django.db import models
import uuid


class Customer(models.Model):
    """Model representing an Customer."""
    customer_id = models.AutoField(primary_key=True)
    customer_uuid = models.UUIDField(default=uuid.uuid4, auto_created=True)
    first_name = models.CharField(max_length=100, help_text="Enter your first name", null=True)
    last_name = models.CharField(max_length=100, help_text="Enter your last name", null=True)
    phone = models.CharField(max_length=15, help_text="Enter your phone number", null=True)
    street_address = models.CharField(max_length=255, help_text="Enter your address", null=True)
    city = models.CharField(max_length=255, help_text="Enter your city", null=True)
    zip_code = models.CharField(max_length=255, help_text="Entry your zip code", null=True)
    referrer = models.ForeignKey('Customer', default=None, on_delete=models.SET_NULL, null=True, blank=True,)


    class Meta:
        ordering = ['customer_id']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.customer_id}, {self.last_name}, {self.first_name}'