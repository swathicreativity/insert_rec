# from django.shortcuts import render, redirect
# from .models import Blog

# # Create Blog
# def create_blog(request):
#     if request.method == "POST":
#         Name = request.POST['Name']
#         Advocate = request.POST['Advocate']
#         Mobile = request.POST['Mobile']
#         Email = request.POST['Email']
#         CaseNo = request.POST['CaseNo']
#         CaseYear = request.POST['CaseYear']
#         CaseType = request.POST['CaseType']
#         CourtName = request.POST['CourtName']
#         CourtArea = request.POST['CourtArea']
#         data = Blog(Name=Name,Advocate=Advocate,Mobile=Mobile,Email=Email,CaseNo=CaseNo,CaseYear=CaseYear,CaseType=CaseType,CourtName=CourtName,CourtArea=CourtArea)
#         data.save()
  
#         return redirect('show/')
#     else:
#         return render(request, 'insert.html')

# # Retrive Employee
        
# def show_blogs(request):
#     blogs = Blog.objects.all()
#     return render(request,'show.html',{'blogs':blogs} )

from django.shortcuts import render, redirect
from .forms import BlogForm
from .models import Blog

# Add Blog

def create_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('show/')
            except:
                pass
    else:
        form = BlogForm()
    return render(request, 'create.html', {'form':form})

# Retrive Employee
        
def show_blogs(request):
    blogs = Blog.objects.all()
    return render(request,'show.html',{'blogs':blogs} )
