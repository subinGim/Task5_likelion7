from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from .forms import BlogForm, CommentForm, HashtagForm
from .models import Blog, Comment, Hashtag

# Create your views here.
def layout(request):
   return render(request, 'blog/layout.html')

def home(request):
   blogs = Blog.objects
   hashtags = Hashtag.objects
   return render(request, 'blog/home.html', {'blogs': blogs, 'hashtags':hashtags})

def create(request):
   # blog = Blog()
   # if request.method == 'POST':
   #    # blog.image = request.FILES['image']
   #    blog.image = request.FILES.get('image')
   #    blog.title = request.POST['title']
   #    blog.body = request.POST['body']
   #    blog.pub_date = timezone.datetime.now()
   #    blog.save()
   #    # h{} = request.GET['hash']
   #    # h = request.POST.get("hash[]")
   #    # for a in h:
   #    #    blog.hashtags.add(a) 
   #    h = request.POST.getlist('hash')
   #    blog.hashtags.set([h]) 
   #    blog.save()
   # return redirect('home')
   blog = Blog()
   blog.title = request.GET['title']
   blog.body = request.GET['body']
   blog.image = request.GET['image'] 
   blog.pub_date = timezone.datetime.now()
   blog.save()
   return redirect('blog/home/') #바로 페이지를 띄워버리는 느낌

def blogform(request, blog=None):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False) #폼에 있는 데이터만 가져옴. 저장X 이때 시간데이터는 가져오지 않았기 때문에.
            blog.pub_date=timezone.now()
            # blog.image = request.FILES['image']
            blog.image = request.FILES.get('image')
            blog.save()
            form.save_m2m()
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

def detail(request, title_id):
   blog = get_object_or_404(Blog, id=title_id)
   if request.method == "POST":
      form = CommentForm(request.POST)
      if form.is_valid():
         comment = form.save(commit=False)
         comment.title_id = blog
         comment.comment_text = form.cleaned_data["comment_text"]
         comment.save()
         return redirect('detail', title_id)
   else:
      form = CommentForm()
      return render(request, "blog/detail.html", {"blog": blog, "form":form})

# def edit_comm(request, pk):
#    comment = get_object_or_404(Comment, pk=pk)
#    return commentform(request, comment)

def edit_comm(request, title_id):
   comment = get_object_or_404(Comment, pk=title_id)
   return commentform(request, comment)


#comment 수정 시 사용할 함수
def commentform(request, comment=None):
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comment_text = form.cleaned_data["comment_text"]
            comment.save()
            return redirect('home')
            # return redirect('detail', comment.title_id)
            # return render(request, 'blog/detail.html', {'comment':comment})
    else:
        #GET방식으로 요청이 들어왔을 때 실행할 코드
        form = CommentForm(instance=comment)
        return render(request, 'blog/edit_comm.html', {'form':form})

def remove_comm(request, pk):
   comment = get_object_or_404(Comment, pk=pk)
   comment.delete()
   # return redirect('detail', comment.title_id)
   return redirect('home')

def hashtagform(request, hashtag=None):
   if request.method == 'POST':
      form = HashtagForm(request.POST, instance=hashtag)
      if form.is_valid():
         hashtag = form.save(commit=False)
         if Hashtag.objects.filter(name=form.cleaned_data['name']):
            form = HashtagForm()
            error_message = "이미 존재하는 해시태그 입니다"
            return render(request, 'blog/hashtag.html', {'form':form, "error_message":error_message})
         else:
            hashtag.name = form.cleaned_data['name']
            hashtag.save()
            return redirect('home')
   else:
      form = HashtagForm(instance=hashtag)
      return render(request, 'blog/hashtag.html', {'form':form})

def search(request, hashtag_id):
   hashtag = get_object_or_404(Hashtag, pk=hashtag_id)
   hashtags = Hashtag.objects
   return render(request, 'blog/search.html', {'hashtag': hashtag, 'hashtags':hashtags})