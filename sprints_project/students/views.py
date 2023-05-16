# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import datetime
from .models import Student
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from .forms import InputForm
from .forms import StudentForm
# from .models import Post
# from .forms import PostForm
# from .import views
# from django.shortcuts import redirect


def Welcome(request):
	return HttpResponse("welcome to our site")

def Show(request):
    
    # template = loader.get_template('show.html')
    # return HttpResponse(template.render())	
    today = datetime.datetime.now().date()
    return render(request,"show.html", {"today" : today}) 

def list_view(request):
	context ={}
	context['dataset'] = Student.objects.all()
	return render(request, "list_view.html",context)

class StudentList(ListView):
	model = Student


class StudentCreate(CreateView):
	#specify the model for create view
	model = Student
	#specify ther fields to be displayed
	fields =['f_name','l_name']


def home_view(request):	
	form = StudentForm(request.POST or None)
	if form.is_valid():
		form.save()
	context={}
	context['form']=InputForm()
	return render(request,"home.html",context)

def home_view2(request):
	#create your views here.
	form = StudentForm(request.POST or None)
	if form.is_valid():
		form.save()

	context={}
	context['Studentform']=StudentForm()
	return render(request,"home2.html",context)

# def home(request):
# 	if request.method =='POST':
# 		details = PostForm(request.POST)


# 		if details.is_valid():
# 			post = details.save(commit = False)
# 			post.save()
# 			return HttpResponse("data submitted successfully")

# 		else:
# 			return render(request,"home3.html",{'form':details})
# 	else:
# 		form = PostForm(None)
# 		return render(request,'home3.html',{'form':form})


# def home(request):
 
#     # check if the request is post
#     if request.method =='POST': 
 
#         # Pass the form data to the form class
#         details = PostForm(request.POST)
 
#         # In the 'form' class the clean function
#         # is defined, if all the data is correct
#         # as per the clean function, it returns true
#         if details.is_valid(): 
 
#             # Temporarily make an object to be add some
#             # logic into the data if there is such a need
#             # before writing to the database  
#             post = details.save(commit = False)
 
#             # Finally write the changes into database
#             post.save() 
 
#             # redirect it to some another page indicating data
#             # was inserted successfully
#             return HttpResponse("data submitted successfully")
             
#         else:
         
#             # Redirect back to the same page if the data
#             # was invalid
#             return render(request, "home.html", {'form':details}) 
#     else:
 
#         # If the request is a GET request then,
#         # create an empty form object and
#         # render it into the page
#         form = PostForm(None)  
#         return render(request, 'home.html', {'form':form})

