from django.db import models



class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    desc = models.TextField()


    def __str__(self):
        return self.name
        #return self.name + ' - ' + self.email
