from django.db import models

# Create your models here.

class Images(models.Model):
    """
    models to handle images
    """
    image = models.ImageField(upload_to='images/')
    date_posted = models.DateTimeField(blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=100)
    posted_by = models.CharField(max_length=40, default='admin')
    category = models.ForeignKey('Categories', on_delete=models.CASCADE, default=1)
    location = models.ForeignKey('Locations', on_delete=models.CASCADE, default=1)
    
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
        image_location = Images.objects.filter(location__name=location).all()
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
        images = cls.objects.filter(category__name__icontains=category)
        return images

class Category(models.Model):
    name = models.CharField(max_length=50)




