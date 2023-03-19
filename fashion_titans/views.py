from django.shortcuts import render

# Create your views here.

from django.shortcuts import get_object_or_404, render
from .models import *
from django.db.models import Q
from django.contrib import messages
from ML_models import main1


# Create your views here.

def home(request):
    catg = Category.objects.all
    # if request.method.POST:
    #     upload = request.POST.get('upload')
    context = {'catg':catg} 
    return render(request, 'home.html', context)


def cloth_classifier(request):
    # from PIL import Image,ImageDraw
    # label_names = ['T-shirt/top','Trouser','Pullover','Dress','Coat','Sandal','Shirt','Sneaker','Bag','Ankle boot']
    if request.method=="POST":
        files = request.FILES  # multivalued dict
        image = files.get("upload")
        # fil=request.POST.get('upload')
    # test = img_to_array(test)
    # image = Image.open(image)
    # main1.predimage(image,label_names)
    # print(image)
    c=recmd(img=image)
    c.save()
    print("hello")
    res="___"
    context = {'res':res} 
    return render(request, 'home.html', context)

def categories(request):
    label_names = ['T-shirt/top','Trouser','Pullover','Dress','Coat','Sandal','Shirt','Shoes','Bag','Ankle boot']
    # pth="./media"
    pth=""
    ls=[]
    mk = recmd.objects.values_list('img')
    for i in mk :
         print(i[0])
         pth= "./media/" + i[0]
         print(pth)
         ls.append(main1.predimage(pth,label_names))
    print(ls)
    # print(x)
    # for i in range(len(ls)):
    catg = Category.objects.filter(category=ls[0])
    catg1 = Category.objects.filter(category=ls[1])
    context = {'catg':catg, 'mk':mk, 'catg1':catg1}    
    return render(request, 'categories.html', context)




def search(request):
    query = request.GET['query']
    if len(query) > 78:
        result_catg = []
    else:
            result_catg = Category.objects.filter(Q(title__contains=query) | Q(desc__contains=query))
    if result_catg.count() == 0:
        messages.error(request, 'No search results found. Please refine your keyword.')

    context = {'result_catg':result_catg, 'query':query}
    return render(request, 'search.html', context)


