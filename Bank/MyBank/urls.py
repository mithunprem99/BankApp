from django.urls import path,include
from . import views
urlpatterns = [
	path('',views.home,name='home'),
	path('login/',views.login,name='login'),
	path('register/',views.register,name='register'),
	path('registerAction/',views.registerAction,name='registerAction'),
	path('loginAction/',views.loginAction,name='loginAction'),
	path('getbranch/',views.getbranch,name='getbranch'),
	path('userHome/',views.userHome,name='userHome'),
	path('formAction/',views.formAction,name='formAction'),
	path('logout/',views.logout,name='logout')

]