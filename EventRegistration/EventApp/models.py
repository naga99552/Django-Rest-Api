from django.db import models

#model for event registration
class EventRegistration(models.Model):

    firstname=models.CharField(max_length=10)
    lastname=models.CharField(max_length=10)
    email=models.EmailField()
    mobile=models.CharField(max_length=10)
    address=models.CharField(max_length=50)

    def __str__(self):
        return self.firstname+" "+self.lastname