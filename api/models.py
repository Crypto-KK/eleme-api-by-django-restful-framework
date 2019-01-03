from django.db import models

class Entry(models.Model):
    city = models.CharField(max_length=50)
    school = models.CharField(max_length=100)
    link = models.CharField(max_length=100,null=True,default='null')
    name = models.CharField(max_length=200)
    lat = models.CharField(max_length=20,null=True,default='0.0')
    lng = models.CharField(max_length=20,null=True,default='0.0')
    address = models.CharField(max_length=200,null=True,default='null')
    distance = models.CharField(max_length=20,null=True,default='0')
    time = models.CharField(max_length=20,null=True,default='0:00')
    contact = models.CharField(max_length=200,null=True,default='null')
    score = models.CharField(max_length=10,null=True,default='0')
    comments = models.CharField(max_length=20,null=True,default='0')
    sell = models.CharField(max_length=20,null=True,default='0')
    image = models.CharField(max_length=200,null=True,default='null')
    owner = models.ForeignKey('auth.User',related_name='entries',on_delete=models.CASCADE)
    # class Meta:
    #     ordering = ('name',)
    def __str__(self):
        return self.name