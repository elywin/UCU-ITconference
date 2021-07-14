from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import *

# Create your views here


def index(request):

    goal = OurGoal.objects.all()
    
    about = AboutUs.objects.all()
    
    faqs = FAQs.objects.all()
        
    titles = EventTitles.objects.all()

    folder2 = 'static/images'
    folder = 'static/files'
    if "register" in request.POST:
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        address = request.POST["address"]
        zip = request.POST["zip"]
        city = request.POST["city"]
        cell = request.POST["cell"]
        country = request.POST["country"]
        picture = request.FILES["pic"]
        fs2 = FileSystemStorage(location=folder2)
        filename2 = fs2.save(picture.name, picture)
        file_url2 = fs2.url(filename2)
        print(file_url2)
        paper_file = request.FILES['paper_file']
        fs = FileSystemStorage(location=folder)
        filename = fs.save(paper_file.name, paper_file)
        file_url = fs.url(filename)
        print(file_url)
        Reginfo = Guest(fname=fname, lname=lname, email=email, address=address,
                        zip=zip, city=city, cell=cell, paper_file=paper_file)
        Reginfo.save()

    return render(request, "index.html",{"OurGoal": goal,"AboutUs":about, "FAQs":faqs, "EventTitles":titles})
