
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404 , render, redirect
from .forms import PostForm
from .models import Post

import os

def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid(): # form 유효성 검사
            # print(form.cleaned_data)
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            # 방법 1)
            # post = Post()
            # post.title = form.cleaned_data['title']
            # post.content = form.cleaned_data['content']
            # post.save()

            # 방법 2)
            # post = Post(title=form.cleaned_data['title'], content=form.cleaned_data['content'])
            # post.save()

            # 방법 3)
            # post = Post.objects.create(title=form.cleaned_data['title'], content=form.cleaned_data['content'])

            # 방법 4)
            # post = Post.objects.create(**form.cleaned_data)
            return redirect('/dojo/')
    else:
        form = PostForm()

    return render(request, 'dojo/post_form.html', { 'form' : form})

def post_edit(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid(): # form 유효성 검사
            # print(form.cleaned_data)
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()

            return redirect('/dojo/')
    else:
        form = PostForm(instance=post)

    return render(request, 'dojo/post_form.html', { 'form' : form})

# Create your views here.
def mysum(request, numbers):
    # request : HttpRequest
    result = sum(map(lambda s: int(s or 0), numbers.split('/')))
    return HttpResponse(result)

def hello(request, name, age):
    return HttpResponse("안녕하세요. {}. {} 살 이시네요".format(name,age))

def post_list1(request):
    name = '공유'
    return HttpResponse(
        '''
        <h1> AskDjango </h1>
        {name}
        '''.format(name=name)
    )

def post_list2(request):
    name = '공유'
    return render(request, 'dojo/post_list2.html', {'name': name})

def excel_download(request):
    filepath = os.path.join(settings.BASE_DIR, 'aaa.xlsx')
    filename = os.path.basename(filepath)

    with open(filepath, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
        return response
