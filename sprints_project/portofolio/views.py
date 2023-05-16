from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Course
from .models import Student
from .models import Post
from django.views.generic.list import ListView
from .forms import PostForm
 

def cv(request):
	template = loader.get_template("cv.html")
	return HttpResponse(template.render())
	#return render(request, "show.html")

class StudentList(ListView):
	model = Student

def course(request):
	context ={}
	context['dataset'] = Course.objects.all()
	return render(request, "courses.html",context)

def home_list(request):
    homes = Post.objects.all()
    return render(request, 'home_list.html', {'homes': homes})


def home(request):
    if request.method == 'POST':
        details = PostForm(request.POST)

        if details.is_valid():
            post = details.save(commit=False)
            post.save()
            return redirect('home_list')

        else:
            return render(request, "home.html", {'form': details})

    else:
        form = PostForm(None)
        return render(request, 'home.html', {'form': form})	