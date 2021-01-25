from django.shortcuts import render

# Create your views here:
def load_files(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'loadfiles.html', {
        'form': form
    })