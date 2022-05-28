from django.shortcuts import render
from .models import Images, Location


# Create your views here.
def index(request):
     images = Images.objects.all()
     locations = Location.get_all_locations()
     return render(request,'index.html',{'images':images ,'locations': locations})

def image_location(request, location):
    images = Images.filter_by_location(location)
    return render(request, 'location.html', {'location_img': images})

def search(request):
    if 'category' in request.GET and request.GET['category']:
        search_term = request.GET.get('category')
        searched_images = Images.search_by_category(search_term)
        message = f'{search_term}'

        return render(request, 'search.html', {'message':message,'images': searched_images})
    else:
        message = "You haven't searched for any image category"
        return render(request, 'search.html', {'message':message})