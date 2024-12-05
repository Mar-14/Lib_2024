from django.http import HttpResponse
from django.shortcuts import redirect, render

from .models import Book
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

from .forms import BookAddForm, MyLoginForm, BookAddForm, UserRegisterationForm
from django.contrib.auth import authenticate,login,logout

def index(request):
    return render(request,'home.html')


def register(request):
    if request.method=='POST':
        #getting username and password
        user_reg_form=UserRegisterationForm(request.POST)
        if user_reg_form.is_valid():
            new_user=user_reg_form.save(commit=False)
            new_user.set_password(user_reg_form.cleaned_data['password'])
            new_user.save()
        return render(request,'useraccount/register_done.html',{'user_reg_form':user_reg_form})
    else:
            user_reg_form=UserRegisterationForm()
    return render(request,'useraccount/register.html',{'user_reg_form':user_reg_form})

def user_login(request):
    if request.method == 'POST':
        #we will be getting username and password through POST
        login_form=MyLoginForm(request.POST)
        if login_form.is_valid():
            cleaned_data=login_form.cleaned_data
            auth_user=authenticate(request, username=cleaned_data['username'],password=cleaned_data['password'])
            if auth_user is not None:
                login(request,auth_user)
                group=auth_user.groups.first()
                group_name=group.name if group else "No Group"
                request.session['group_name']=group_name
                return redirect('home_path')
                
            else:
                return HttpResponse('Not Authenticated')
    else:
        login_form=MyLoginForm()
    return render(request,'useraccount/login_form.html',{'login_form':login_form})



def custom_logout(request):
    logout(request)

    return redirect('login')

from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Book

def book_list(request):
    # Fetch the input value from the request
    searchTerm = request.GET.get('searchbook')
    if searchTerm:
        book_list = Book.objects.filter(title__icontains=searchTerm)
    else:
        book_list = Book.objects.all()

    # Set up pagination
    paginator = Paginator(book_list, 5)  # Show 5 books per page
    page = request.GET.get('page')

    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    # Render the template with the context
    return render(request, 'books.html', {'searchTerm': searchTerm, 'book_list': books, 'page': page})



def add_books(request):
    
    if request.method=='POST':
        add_book_form=BookAddForm(request.POST,request.FILES)
        if add_book_form.is_valid():
            
            add_book_form.save()
            return redirect('home_path')
    else:
         add_book_form=BookAddForm()
    return render(request,'add_books.html',{'add_book_form':add_book_form})



