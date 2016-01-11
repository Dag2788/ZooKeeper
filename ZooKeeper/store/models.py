from django.db import models

# Create your models here.

class Pets(models.Model):
    '''
    Pets the store carries
    '''
    name = models.CharField(max_length = 100)
    classification = models.CharField(max_length=100)
    description = models.TextField()
    picture = models.ImageField(upload_to = 'ZooKeeper/static/database/db_animals/images', default = 'ZooKeeper/static/database/db_animals/images/')
    video = models.FileField(upload_to = 'ZooKeeper/static/database/db_animals/videos', default = 'ZooKeeper/static/database/db_animals/videos/')
    # coords = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    climate = models.CharField(max_length= 100)
    pet_care = models.TextField()
    recommended_products = models.TextField()

    def __str__(self):
        return '%s' % (self.name)

    # def __str__(self):
    #     return '%s %s %s %s %s %s %s %s %s %s %s' % (self.classification, self.species, self.description, self.pictures, self.videos, self.coords, self.size, self.climate, self.pet_info)



class Products(models.Model):
    '''
    The products the store carries
    '''
    name = models.CharField(max_length=100)
    description = models.TextField()
    picture = models.ImageField(upload_to = 'ZooKeeper/static/database/db_products/images', default = 'ZooKeeper/static/database/db_products/images/')
    videos = models.FileField(upload_to = 'ZooKeeper/static/database/db_products/videos', default = 'ZooKeeper/static/database/db_products/videos/')
    pets_recommended_for = models.TextField()

    def __str__(self):
        return '%s' % (self.name)
    # def __str__(self):
    #     return '%s %s %s %s %s %s %s' % (self.name, self.description, self.pictures,
    #             self.videos, self.for_pets)
