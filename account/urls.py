from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginPage, name="login"),  
	path('register/', views.registerPage, name="register"),
	path('logout/', views.logoutUser, name="logout"),
	path('lupa/', views.lupa, name="lupa"),
	path('lupaada/', views.lupaada, name="lupaada"),
	path('lupatidak/', views.lupatidak, name="lupatidak"),
	path('GantiPassword/', views.GantiPassword, name="GantiPassword"),
]