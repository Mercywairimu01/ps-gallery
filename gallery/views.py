from django.shortcuts import render
from .models import Images, Location,Category


# Create your views here.
def index(request):
     images = Images.objects.all()
     locations = Location.objects.all()
     if request.GET.get('location'):
         images=Images.objects.filter(location__city=request.GET.get('location'))
         return render(request,'index.html',{'images':images ,'location_img': locations})
     return render(request,'index.html',{'images':images ,'location_img': locations})



def image_location(request,location):
    images = Images.objects.get(location=location)
    return render(request, 'location.html', {'location_img': images})

def search(request):
    if 'category' in request.GET and request.GET['category']:
        search_category = request.GET.get('category')
        searched_images = Images.search_by_category(search_category)
        message = f'{search_category}'
        print(searched_images)

        return render(request, 'search.html', {'message':message,'location_img': searched_images})
    else:
        message = "You haven't searched for any image category"
        return render(request, 'search.html', {'message':message})