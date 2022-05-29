from django.test import TestCase
from .models import Images, Category, Location

# Create your tests here.

class TestImages(TestCase):
    def setUp(self):
        '''
        test method to create Image instances called before all tests
        '''
        self.location = Location(city='Nairobi')
        self.location.save_location()
        
        self.category = Category(name='Nature')
        self.category.save_category()
        
        self.img = Images(id=1, title='image', description='nature at its best', location=self.location,category=self.category)
        
    def test_instance(self):
        '''
        test method to assert instances created during setUp
        '''
        self.assertTrue(isinstance(self.img, Images))   
        
    def test_save_image(self):
        '''
        test method to ensure an Image instance has been correctly saved
        '''
        self.img.save_image()
        img = Images.objects.all()
        self.assertTrue(len(img) > 0)
        
    def test_delete_image(self):
        '''
        test method to ensure an Image instance has been correctly deleted
        '''
        self.img.delete_image()
        images = Images.objects.all()
        self.assertTrue(len(images) == 0)
        
    def test_search_image_by_location(self):
        '''
        test method to obtain image insatnces by location
        '''
        self.img.save_image()
        found_images = self.img.filter_by_location(location='Nairobi')
        self.assertTrue(len(found_images) == 1)
        
    def test_get_image_by_id(self):
        '''
        test method to ensure Image instances can be retrieved by id
        '''
        obtained_image = Images.get_image_by_id(self.img.id)
        
    def test_search_by_category(self):
        '''
        test method to ensure correct searching of an multiple image instances by category
        '''
        obtained_image = Images.search_by_category(self.img.category)
        
    def test_update_image(self):
        '''
        test method to ensure an Image instance has been correctly updated
        '''
        self.img.save_image()
        self.img.update_image(self.img.id, 'images/nature.jpg')
        updated_img = Images.objects.filter(image='images/nature.jpg')
        self.assertTrue(len(updated_img) > 0)
        
        # location tests
        
class TestLocation(TestCase):
    '''
    test class for Locations model
    '''
    def setUp(self):
        '''
        test method to create Location instances called before all tests
        '''
        self.location = Location(city='Nairobi')
        self.location.save_location() 
        
    def test_instance(self):
        '''
        test method to assert instances created during setUp
        '''
        self.assertTrue(isinstance(self.location, Location)) 
                 
    def test_delete_location(self):
        '''
        test method to ensure a Location instance has been correctly deleted
        '''
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)
        
    def test_get_all_locations(self):
        '''
        test method to ensure all instances of Locations class have been retrieved
        '''
        locations = Location.get_all_locations()
       
        
    def test_save_location(self):
        '''
        test method to ensure a Location instance has been correctly saved
        '''
        self.assertTrue(len(Location.objects.all()) == 1)     
    
    
    # def test_update_location(self):
    #     '''
    #     test method to ensure a Location instance has been correctly updated
    #     ''' 
    #     update_term = 'kigali'
    #     self.location.save_location()
    #     Location.update_location(self.location.id, update_term)  
    #     updated_one = Location.objects.get(id=self.location.id)
    #     self.assertEqual(updated_one.location, 'kigali')
    
class TestCategory(TestCase):
    '''
    test class for Categories model
    '''
    def setUp(self):
        '''
        test method to create Category instances called before all tests
        '''
        self.category = Category(name='Nature')
        self.category.save_category()
    def test_instance(self):
        '''
        test method to assert Category instances are created during setUp
        '''
        self.assertTrue(isinstance(self.category, Category))
        
    def test_delete_category(self):
        '''
        test method to ensure a Category instance has been correctly deleted
        '''
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)
        
   