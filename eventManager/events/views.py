from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from .models import Guest
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


# Create your views here

def index(request):
   
    folder='static/files'
    # if request.method == "POST":
    if "register" in request.POST:
            fname = request.POST["fname"]
            lname = request.POST["lname"]
            email = request.POST["email"]
            address = request.POST["address"]
            zip = request.POST["zip"]
            city = request.POST["city"]
            cell = request.POST["cell"]
            country = request.POST["country"]
            paper_file = request.FILES['paper_file']
            fs = FileSystemStorage(location=folder)
            filename = fs.save(paper_file.name, paper_file)
            file_url = fs.url(filename)
        #   print(file_url)
            print(file_url)
            Reginfo = Guest(fname=fname,lname=lname,email=email,address=address,zip=zip,city=city,cell=cell,paper_file=paper_file)
            
            Reginfo.save()
            
          
    return render(request, "index.html")

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            return redirect('posts:list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('posts:list')