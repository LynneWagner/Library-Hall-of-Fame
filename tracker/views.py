from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm
from .models import Item
from .models import Book
from .models import DVD
from .models import Mags
from .models import Newspaper
from .models import Music


import _json

def index(request):
    query = request.GET.get('query')
    if query:
        
        items = Item.objects.filter(Q(name__icontains=query) | Q(description__icontains=query) | Q(creator__icontains=query))
        return render(request, 'tracker/search.html', context={'items':items})

    else:
        all_books = Book.objects.all()
        all_dvds = DVD.objects.all()
        all_mags = Mags.objects.all()
        all_newspapers = Newspaper.objects.all()
        context_dict = {'all_books': all_books, 'all_dvds':all_dvds, 'all_mags':all_mags, 'all_newspapers':all_newspapers}
        return render(request, 'tracker/index.html', context=context_dict)

def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'tracker/detail.html', {'book': book})

def dvd_detail(request, dvd_id):
    dvd = get_object_or_404(DVD, pk=dvd_id)
    return render(request, 'tracker/dvd_detail.html', {'dvd': dvd})

def mags_detail(request, mag_id):
    mag = get_object_or_404(Mags, pk=mag_id)
    return render(request, 'tracker/mags_detail.html', {'mag': mag})

def newspaper_detail(request, newspaper_id):
    newspaper = get_object_or_404(Newspaper, pk=newspaper_id)
    return render(request, 'tracker/newspaper_detail.html', {'newspaper': newspaper})

def music_detail(request, music_id):
    nmusic = get_object_or_404(Music, pk=music_id)
    return render(request, 'tracker/music_detail.html', {'music': music})

class UserFormView(View):
    form_class = UserForm
    template_name = 'tracker/register.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #returns user objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('tracker:index')

            return render(request, self.template_name, {'form':form})

