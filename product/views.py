from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.decorators.http import require_http_methods
from .models import Product
from food_app.common import get_name_slug, get_file_type, check_auth
from django.core.files.storage import FileSystemStorage
from category.models import Category
from image.models import Image

# Create your views here.


@require_http_methods(['GET'])
def index(request):
    check_auth(request)
    data = Product.objects.all()
    context = {
        'data':data
    }

    return render(request,'product/list.html',context)

@require_http_methods(['GET'])
def add(request):
    check_auth(request)
    cate_data = Category.objects.all()
    context = {
        'cate_data':cate_data
    }
    return render(request, 'product/form.html', context)

@require_http_methods(['POST'])
def save(request, id):
    check_auth(request)
    data = request.POST
    if id is None:
        if request.method == 'POST' and request.FILES:
            path_img = handle_uploaded_file(request.FILES['image'])
        else:
            path_img = ''
        img_title = get_name_slug(data['name'])
        image = Image.objects.create(title=img_title, path=path_img)
        category = Category.objects.create(
            name=data['name'], description=data['description'], price=data['price'], category_id = data['cate_id'], status=data['status'], image_id=image.id)
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
