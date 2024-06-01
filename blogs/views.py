
from django.shortcuts import get_object_or_404, redirect, render

from blogs.models import Blog, Category
from django.db.models import Q

# Create your views here.

def posts_by_category(request, category_id):

    # Fetch the posts that belongs to the category with the id category_id
    posts=Blog.objects.filter(status='Published', category=category_id)  # if we put category_id=category_id then also works

    # Use try/except when we want to do some custom action if the category doesnt exist
    # try:
    #     category = Category.objects.get(pk=category_id)
    # except:
    #     # redirect the user to homepage
    #     return redirect('home')
    
    # Use get_object_or_404 when you want to show 404 error page if category doesnt exist
    category=get_object_or_404(Category, pk=category_id)

    context ={
        'posts': posts,
        'category': category, 
    }

    
    return render(request,'posts_by_category.html',context)

def blogs(request, slug):
    single_blog=get_object_or_404(Blog, slug=slug, status='Published')
    context= {
        'single_blog': single_blog
    }

    return render(request, 'blogs.html',context)

def search(request):
    keyword= request.GET.get('keyword')
    blogss=Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword),status='Published')
    context={
        "blogss":blogss,
        "keyword":keyword,
    }
    
    return render(request,'search.html',context)