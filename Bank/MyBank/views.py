from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
# Create your views here.

def home(request):
	district_tb=District.objects.all()
	return render(request,'HomePage.html',{'views':district_tb})

def login(request):
	return render(request,'login.html')


def register(request):
	return render(request,'Register.html')




def registerAction(request):
	username=request.POST['username']
	password=request.POST['password']
	confirm=request.POST['cpassword']
	if password == confirm:
		register_tb=RegisterModel(Username=username,Password=password)
		register_tb.save()
		messages.add_message(request,messages.INFO,username+"Registered Sucessfully")
		return render(request,'login.html')
	else:
		messages.add_message(request,messages.INFO,"Password doesnot matches")
		return redirect('/')

def loginAction(request):
	username= request.POST['username']
	password=request.POST['password']
	user_tb=RegisterModel.objects.filter(Username=username,Password=password)
	if user_tb.count()>0:
		request.session['id']= user_tb[0].id
		district_tb=District.objects.all()
		return render(request,'userhome.html',{'views':district_tb})
	else:
		messages.add_message(request,messages.INFO,"User Not exist")
		return redirect('login')

def userHome(request):
	district_tb=District.objects.all()
	return render(request,'userhome.html',{'views':district_tb})

def getbranch(request):
	d_id=request.GET['branch']
	branch_tb=BranchModel.objects.filter(District=d_id)
	return render(request,'getBranch.html',{'branch':branch_tb})

def formAction(request):
	if request.method == "POST":
		user=request.session['id']
		name=request.POST['name']
		dob=request.POST['dob']
		age=request.POST['age']
		gender=request.POST['gender']
		phone=request.POST['phone']
		email=request.POST['email']
		address=request.POST['address']
		district=request.POST['district']
		branch=request.POST['branch']
		account=request.POST['acc']
		materials=request.POST.getlist('materials')
		application_tb=ApplicationModel(User_id=user,Name=name,DOB=dob,Age=age,Gender=gender,Phone=phone,Email=email,Address=address,District_id=district,Branch_id=branch,Account=account,Materials=materials)
		application_tb.save()
		messages.add_message(request,messages.INFO,"Application Accepted")
		return redirect('userHome')	


def logout(request):
	request.session.clear()
	return redirect('/')

