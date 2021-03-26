from django.shortcuts import render

# Create your views here.

def home(request):
    context = {

    }
    return render(request, 'blog_app/home.html', context)


def blog(request):
    context = {

    }
    return render(request, 'blog_app/blog.html', context) 