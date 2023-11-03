from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm


def Create(request):
    if request.method == "POST":
        fm = ContactForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('read')
    else:
        fm = ContactForm()
    return render(request, 'index.html', {'fm': fm})


def Read(request):
    data = Contact.objects.all()
    return render(request, 'read.html', {'data': data})


def Update(request, id):
    cont = get_object_or_404(Contact, id=id)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=cont)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ContactForm(instance=cont)
        return render(request, 'index.html', {'form': form})

    def Delete(request, id):
        cont = get_object_or_404(Contact, id=id)
        cont.delete()
        return redirect('/')
