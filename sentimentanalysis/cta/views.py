from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import json
from . import dest
from . import graph_data

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    obj=graph_data.Data('india')
    data=obj.getdata()
    overall=obj.overall_data
    context = {
        'data':data,
        'overall':overall
    }
    return HttpResponse(template.render(context,request))

def major_cities(request):

    Mumbai=dest.Cities('Mumbai','https://res.cloudinary.com/dseemci6h/image/upload/v1594205707/Mumbai_nmtl78.webp',graph_data.Data('Mumbai').overall_data)
    Delhi = dest.Cities('Delhi', 'https://res.cloudinary.com/dseemci6h/image/upload/v1594205702/Delhi_hihvem.jpg',graph_data.Data('Delhi').overall_data)
    Kolkata = dest.Cities('Kolkata', 'https://res.cloudinary.com/dseemci6h/image/upload/v1594205703/Kolkata_cxzrkl.jpg', graph_data.Data('Kolkata').overall_data)
    Chennai = dest.Cities('Chennai', 'https://res.cloudinary.com/dseemci6h/image/upload/v1594205702/Chennai_elym5i.jpg', graph_data.Data('Chennai').overall_data)
    cities=[Mumbai, Delhi, Kolkata, Chennai]
    return render(request, 'major_cities.html', {'cities':cities})

def city(request,city_name):
    template = loader.get_template('cities.html')
    obj = graph_data.Data(city_name)
    data = obj.getdata()
    overall = obj.overall_data
    context = {
        'city_name': city_name,
        'data': data,
        'overall': overall
    }
    return HttpResponse(template.render(context, request))

def about_us(request):
    return render(request,'user.html')