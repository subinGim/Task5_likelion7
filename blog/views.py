from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from .forms import BlogForm
from .models import Blog

# Create your views here.
def layout(request):
   return render(request, 'blog/layout.html')

def home(request):
   blogs = Blog.objects
   return render(request, 'blog/home.html', {'blogs': blogs})

def new(request):
    return render(request, 'blog/new.html') #해당 페이지에 데이터까지 포함해서 전달하는 느낌

def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blog/home/') #바로 페이지를 띄워버리는 느낌

def blogform(request, blog=None):
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False) #폼에 있는 데이터만 가져옴. 저장X 이때 시간데이터는 가져오지 않았기 때문에.
            blog.pub_date=timezone.now()
            blog.save()
            return redirect('home')
    else:
        #GET방식으로 요청이 들어왔을 때 실행할 코드
        form = BlogForm(instance=blog)
        return render(request, 'blog/edit.html', {'form':form})

def edit(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return blogform(request, blog)

def remove(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return redirect('home')