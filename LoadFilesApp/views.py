from django.shortcuts import render

from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage

# Create your views here:
class Home(TemplateView):
    template_name = 'home.html'

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        #print(uploaded_file.name)
        #print(uploaded_file.size)
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
        #print(url)
    return render(request, 'upload.html', context)