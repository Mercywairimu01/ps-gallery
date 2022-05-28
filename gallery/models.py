from django.db import models

# Create your models here.

class Images(models.Model):
    """
    models to handle images
    """
    image = models.ImageField(upload_to='images/')
    date_posted = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=100)
    posted_by = models.CharField(max_length=40, default='admin')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default=1)
    location = models.ForeignKey('Location', on_delete=models.CASCADE, default=1)
    
    def __str__(self):
        return self.title
    
    
    def save_image(self):
        '''
        method to save an image
        '''
        self.save()

    def delete_image(self):
        '''
        method to delete an image
        '''
        self.delete()
    
    @classmethod
    def get_all(cls):
        '''
        method to get all images
        '''
        images = Images.objects.all()
        return images

    @classmethod
    def filter_by_location(cls, location):
        '''
        method to get images by their locations
        '''
        image_location = Images.objects.filter(location__city=location).all()
        return image_location

    @classmethod
    def update_image(cls, id, value):
        '''
        method to update an image
        '''
        cls.objects.filter(id=id).update(image=value)

    @classmethod
    def get_image_by_id(cls, id):
        '''
        method to get images by unique id
        ''' 
        image = cls.objects.filter(id=id).all()
        return image

    @classmethod
    def search_by_category(cls, category):
        '''
        method to search images by category
        '''
        images = cls.objects.filter(category__name__contains=category)
        return images

class Category(models.Model):
    name = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.name

    def save_category(self):
        '''
        method to save a category
        '''
        self.save()

    def delete_category(self):
        '''
        method to delete a category
        '''
        self.delete()

class Location(models.Model):
    '''
    model to handle locations
    '''
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    
    def __str__(self):
        return self.country

    def save_location(self):
        '''
        method to save a location
        '''
        self.save()

    def delete_location(self):
        '''
        method to delete a location
        '''
        self.delete()

    @classmethod
    def update_location(cls, id, value):
        '''
        method to update a location's name
        '''
        cls.objects.filter(id=id).update(image=value)
    @classmethod
    def get_all_locations(cls):
        '''
        method to retrive all stored locations
        '''
        cities = Location.objects.all()
        return cities


