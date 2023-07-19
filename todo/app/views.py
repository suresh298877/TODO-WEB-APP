from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import SignUpForm
from django.contrib.auth import authenticate,login as loginuser,logout
from django.contrib.auth.decorators import login_required
from .models import TODO,user_gmail_verificatoin_list
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import TODOForm
from django.contrib.auth.models import User
# from .models import Profile
import uuid
from .utils import send_email_token
# Create your views here.
@login_required(login_url='login')
def home(request):
    todos=None
    if request.user.is_authenticated:
        todos=TODO.objects.filter(user = request.user).order_by('priority')
    form=TODOForm()
    u='AnonymousUser'
    h='TODO'
    if str(request.user)!=u:
        h=str(request.user)+" "+h
    

    # print(request.user)
    return render(request,'index.html',context={'form':form,'h':h,'todos':todos})

def login(request):
    u='AnonymousUser'
    h='TODO'
    if str(request.user)!=u:
        h=str(request.user)+" "+h
    if request.method=='GET':
        form=AuthenticationForm()
        context={
            'form':form,
            'h':h
        }

        return render(request,'login.html',context)
    else:
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            # print(user)
            if user is not None:
                loginuser(request,user)
                return redirect('home')
        else:
            context={
                'form':form,
                'h':h
            }
            return render(request,'login.html',context)

def logoutUser(request):
    print(request)
    logout(request)
    return redirect('home')
def signup(request):
    # if request.method=='POST':
    #     name=request.POST.get('name')
    #     mail=request.POST.get('mail')
    #     pwd1=request.POST.get('pwd1')
    #     pwd2=request.POST.get('pwd2')
    #     if pwd1!=pwd2:
    #         return HttpResponse("Enter password correctly")
    #     else:
    #         return HttpResponse("successfully registered")
    # return render(request,'signup.html')
    u='AnonymousUser'
    h='TODO'
    if str(request.user)!=u:
        h=str(request.user)+" "+h
    if request.method=='GET':
        form=SignUpForm()
        context={
            'form':form,
            'h':h
        }
        return render(request,'signup.html',context)
    else:
        # form=SignUpForm(request.POST)
        # print(request.POST.get('email'))
        # print(request.POST.get('password1'))
        fname=request.POST.get('first_name')
        lname=request.POST.get('last_name')
        uname=request.POST.get('username')
        e=request.POST.get('email')
        psswd=request.POST.get('password1')
        email_token=str(uuid.uuid4())


        u_obj=user_gmail_verificatoin_list.objects.create(
            email=e,
            password=psswd,
            token=email_token,
            firstn=fname,
            lastn=lname,
            usern=uname
            
        )
        # # user_gmail_verificatoin_list.objects.get(email=e).delete()
        try:
            send_email_token(e,email_token)
            return HttpResponse("we have sent an verification email to you.")
        except Exception as e:
            print('exception occured at signup page send mail \n',e)

        # try:
        #     if form.is_valid:
        #         user=form.save()
        #         if user is not None:
        #             return redirect('home')
        # except:
        #     return HttpResponse("user is already registered or password is mismatched")
        



    if form.is_valid:
        pass
    else:
        form=SignUpForm()
    context={
        'form':form,
        'h':h
    }
    return render(request,'signup.html',context)

def todo(request):
    if request.user.is_authenticated:
        print(request.user)
        form=TODOForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            tod=form.save(commit=False)
            tod.user=request.user
            tod.save()
            print(tod)
            return redirect('home')
        else:
            return render(request,'index.html',context={'form':form})
    else:
        return HttpResponse("<h1>Please login before adding todo's</h1>")

def delete_todo(request,id):
    TODO.objects.get(pk=id).delete()
    return redirect('home')
    
def change_todo(request,id,status):
    todoo=TODO.objects.get(pk=id)
    todoo.status=status
    todoo.save()
    return redirect('home')


def ghome(request):
    if request.method == 'POST':
        e=request.POST.get('email')
        psswd=request.POST.get('password1')
        email_token=str(uuid.uuid4())
        u_obj=user_gmail_verificatoin_list.objects.create(
            email=e,
            password=psswd,
            token=email_token
        )
        # user_gmail_verificatoin_list.objects.get(email=e).delete()
        try:
            send_email_token(e,email_token)
        except Exception as e:
            print('exception occured at ghome send mail \n',e)

    return render(request,'ghome.html')

def gverify(request,token):
    token=str(token)
    try:
        # obj=Profile.objects.get(email_token=token)
        # obj.is_verified=True
        # obj.save()
        # user=obj.user
        # user.delete()
        # o=User.objects.get(username=)
# fields=['first_name','last_name','username','email','password1','password2']

        obj=user_gmail_verificatoin_list.objects.get(token=token)
        # form=SignUpForm(first_name=obj.firstn,last_name=obj.lastn,username=obj.usern,email=obj.email,password1=obj.password,password2=obj.password2)
        # form.save()
        uobj=User(first_name=obj.firstn,last_name=obj.lastn,username=obj.usern,email=obj.email)
        uobj.set_password(obj.password)
        uobj.save()
        obj.delete()
        return HttpResponse("Your account verified.Go back to login page.")
    except Exception as e:
        return HttpResponse("Invalid token")








# def homee(request):
#     if request.method == 'POST':
#         email=request.POST.get('email')
#         password=request.POST.get('password')
#         user_obj=User(username=email)
#         user_obj.set_password(password)
#         user_obj.save()
#         p_obj=Profile.objects.create(
#             user=user_obj,
#             email_token=str(uuid.uuid4())

#         )
#         print('helsosidnffo')
#         try:

#             send_email_token(email,p_obj.email_token)
#         except:
#             print('exception occured')
#     return render(request,'home.html')

# def verify(request,token):
#     token=str(token)
#     try:
#         obj=Profile.objects.get(email_token=token)
#         obj.is_verified=True
#         obj.save()
#         # user=obj.user
#         # user.delete()
#         # o=User.objects.get(username=)
#         return HttpResponse("Your account verified")
#     except Exception as e:
#         return HttpResponse("Invalid token")















