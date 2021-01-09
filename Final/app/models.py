"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):

    OPTIONS_PROFILE_TYPE = (
        ('single', 'Single'),
        ('family', 'Family'),
    )

    OPTIONS_LOCATIONS = (
        ('India', 'India'),
        ('Canada', 'Canada'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, help_text='User Name')
    display_name = models.CharField(null=True, max_length = 16, help_text='Optional Display Name' )
    profile_type = models.CharField(null=True, choices=OPTIONS_PROFILE_TYPE, max_length=10)
    location = models.CharField(null=True, max_length = 30, choices=OPTIONS_LOCATIONS, help_text='Optional Location')
    biography = models.CharField(null=True, blank=True, max_length = 500, help_text='Optional Biography')
    
    """ Future Fields"""
    # home_address
    # office_address
    # home_phone
    # office_phone
    # facebook
    # instagram
    # linkedin

    # Metadata
    class Meta:
        ordering = ['profile_type']

    
    # This method was not implemented here. Instead it was sent into the views section to reverse the views as desired.
    # Stack Overflow followup is needed:
    # Methods
    def get_absolute_url(self):
        #Returns the url to access a particular instance of MyModelName.
        return reverse('profile-detail', args=[str(self.id)])

    def __str__(self):
        #String for representing the MyModelName object (in Admin site etc.).
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


"""
class MyModelName(models.Model):
    #A typical class defining a model, derived from the Model class.

    # Fields
    my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')
    ...

    # Metadata
    class Meta:
        ordering = ['-my_field_name']

    # Methods
    def get_absolute_url(self):
        #Returns the url to access a particular instance of MyModelName.
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        #String for representing the MyModelName object (in Admin site etc.).
        return self.my_field_name
"""