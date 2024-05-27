from django.shortcuts import render
from .models import Student,Query
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def register(request):
    return render(request,'register.html')
def expert(request):
    return render(request,'expert.html')

def login(request):
    return render(request,'login.html')

def registerdata(request):
    if request.method == 'POST':
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        contact = request.POST.get('Contact')
        password = request.POST.get('Password')
        cpassword = request.POST.get('Cpassword')

        data = Student.objects.filter(Email=email)
        if data:
            msg = 'user already exit'
            return render(request,'register.html',{'key':msg})
        else:
            if password == cpassword:
                Student.objects.create(Name=name,
                                        Email = email,
                                        Contact = contact,
                                        Password= password)
                msg="Registration Successfully"
#for email
                subject="Test_Mail from Django server"
                message="New member registered"
                from_email="sumitumariya11@gmail.com"
                recipient_list=["sumitumariya11@gmail.com","asumitumariya11@gmail.com "]

                send_mail(subject,message,from_email,recipient_list)

                return render(request,'login.html',{'key':msg})
            
            else:
                msg = "Password & conform password not macthed"
                
                return render(request,'register.html',{'key':msg})

    

def logindata(request):
    # print(request.POST)
    email = request.POST.get('email')
    password = request.POST.get('password')
    # print(password)

    user = Student.objects.filter(Email=email)
    if user:
        data = Student.objects.get(Email = email)
        passs = data.Password
        # print(passs)
        if passs == password:
            Nm = data.Name
            Em = data.Email
            Cm = data.Contact
            Ps = data.Password
            context = {
                'Nm':Nm,
                'Em':Em,
                'Cm':Cm,
                'Ps':Ps
            }
            return render(request,'dashboard.html',{'context':context})
        else:
            msg = "Email & password not matched"
            return render(request,'login.html',{'key':msg})
    
    else:
        msg = "enter valid Email_ID"
        return render(request,'login.html',{'key':msg})

def logout(request):
    return render(request,'home.html')

def Querydata(request):
    # print(request.method)
    # print(request.POST)
    if request.method == "POST":
        email = request.POST.get('email')
        title = request.POST.get('title')
        description = request.POST.get('description')
        # print(email,title,description)
        Query.objects.create(Email=email,
                                 Title = title,
                                 discription = description)
        data = Student.objects.get(Email=email)
        context = {
                'Nm':data.Name,
                'Em':data.Email,
                'Cm':data.Contact,
                'Ps':data.Password
            }
        return render(request,'dashboard.html',{'context':context})
    
def Show(request):
    
    if request.method == "POST":
        email = request.POST.get('email')
        QueryData = Query.objects.filter(Email = email)
        data = Student.objects.get(Email=email)
        context = {
                'Nm':data.Name,
                'Em':data.Email,
                'Cm':data.Contact,
                'Ps':data.Password,
            }
        return render(request,'dashboard.html',{'context':context,'QueryData':QueryData})
        
        
def delete(request,pk,ml):
        del1 = Query.objects.get(id=pk)
        del1.delete()
   
        QueryData = Query.objects.filter(Email = ml)
        data = Student.objects.get(Email= ml)
        context = {
                'Nm':data.Name,
                'Em':data.Email,
                'Cm':data.Contact,
                'Ps':data.Password,
            }
        return render(request,'dashboard.html',{'context':context,'QueryData':QueryData})

def editpage(request,pk):
    data1 = Query.objects.get(id = pk)
    email = data1.Email

    data2 = Student.objects.get(Email = email)
    name = data2.Name
    email = data2.Email
    contact = data2.Contact
    password = data2.Password
    context = {
        'Nm':name,
        'Em':email,
        'Cm':contact,
        'Ps':password
    }
    alldata = Query.objects.filter(Email = email)
    return render(request,'dashboard.html',{'key1':alldata,'context':context,'key2':data1})

def updatedata(request,pk):
    print(request.POST)
    print(pk)
    udata = Query.objects.get(id =pk)
    udata.Email = request.POST['email']
    udata.Title = request.POST['title']
    udata.discription = request.POST['description']
    
    udata.save()
    data = Student.objects.get(Email = udata.Email)
    name = data.Name
    email = data.Email
    contact = data.Contact
    password = data.Password
    context = {
        'Nm':name,
        'Em':email,
        'Cm':contact,
        'Ps':password
    }
    alldata = Query.objects.filter(Email = email)
    return render(request,'dashboard.html',{'key1':alldata,'context':context})