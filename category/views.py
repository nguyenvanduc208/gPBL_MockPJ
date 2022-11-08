from django.shortcuts import HttpResponse, render
from django.core.files.storage import FileSystemStorage
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect
from uuid import uuid4
from .models import Category
from image.models import Image
from food_app.common import get_file_type, get_name_slug, check_auth
from django.contrib.auth.decorators import login_required
# Create your views here.


@require_http_methods(['GET'])
@login_required(login_url='login')
def index(request):
    data = Category.objects.all()
    context = {
        "data": data
    }

    return render(request, 'category/list.html', context)


@require_http_methods(['GET'])
@login_required(login_url='login')
def add(request):
    return render(request, 'category/form.html')


@require_http_methods(['POST'])
@login_required(login_url='login')
def save(request, id=None):
    data = request.POST
    if id is None:
        if request.method == 'POST' and request.FILES:
            path_img = handle_uploaded_file(request.FILES['image'])
        else:
            path_img = ''
        img_title = get_name_slug(data['name'])
        image = Image.objects.create(title=img_title, path=path_img)
        category = Category.objects.create(
            name=data['name'], description=data['description'], status=data['status'], image_id=image.id)
    else:
        cate = Category.objects.get(pk=id)
        cate.name = data['name']
        cate.description = data['description']
        cate.status = data['status']
        if request.method == 'POST' and request.FILES:
            img_title = get_name_slug(data['name'])
            path_img = handle_uploaded_file(request.FILES['image'])
            image = Image.objects.create(title=img_title, path=path_img)
            cate.image_id = image.id

        cate.save()

    return redirect('index')


def handle_uploaded_file(file_input):
    upload = file_input
    fss = FileSystemStorage()
    file_type = get_file_type(upload.name)
    file = fss.save(str(uuid4())+'.'+file_type, upload)
    file_url = fss.url(file)
    return file_url


@require_http_methods(['GET'])
@login_required(login_url='login')
def edit(request, id):
    data = Category.objects.get(pk=id)
    context = {
        "data": data
    }
    return render(request, 'category/form.html', context)


@require_http_methods(['GET'])
@login_required(login_url='login')
def remove(request, id):
    cate = Category.objects.get(pk=id)
    cate.delete()
    return redirect('index')
