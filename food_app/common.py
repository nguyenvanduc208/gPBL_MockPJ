import unicodedata
from django.shortcuts import redirect


def get_file_type(file_name: str):
    file_name = file_name.split('.')
    file_type = file_name[len(file_name)-1]
    return file_type


def get_name_slug(name):
    formatted_name = name.lower().replace(' ', '-').replace('ı', 'i')
    slug = unicodedata.normalize(
        'NFD', formatted_name).encode('ascii', 'ignore')

    return slug.decode('utf-8')

def check_auth(request):
    if request.user.is_authenticated:
        return redirect('login')
