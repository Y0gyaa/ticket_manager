from django.contrib import admin
from django.urls import include, path
from tickets import views as user_view
from django.contrib.auth import views as auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tickets/', include('tickets.urls')),
    path('', include('tickets.urls')),
    path('login/', user_view.Login, name ='login'),
    path('logout/', user_view.Logout, name ='logout'),
    path('register/', user_view.register, name ='register'),
    path('all_tickets/', user_view.All_tickets_view, name='status'),
]
