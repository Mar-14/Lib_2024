from django.shortcuts import render

# Create your views here.
# def user_login(request):
#     if request.method=='POST':
#         #we will be getting username and password through POST
#         login_form=MyLoginForm(request.POST)
#         if login_form.is_valid():
#             clesned_data=login_form.cleaned_data
#             auth_user=authenticate(request,username=clesned_data['username'],password=clesned_data['password'])
#             if auth_user is not None:
#                 login(request,auth_user)
#                 #get the user's group name
#                 group=auth_user.groups.first() #assumes a user has
#                 group_name =group.name if group else "No Group"
#                 request.session['group_name'] = group_name
#                 return redirect('home_path')
#             else:
#                 return HttpResponse('Not Authenticated')
#     else:
#         login_form=MyLoginForm()
#     return render(request,'useraccount/login_form.html',{'login_form':login_form})
