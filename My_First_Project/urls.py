
from django.contrib import admin
from django.urls import path
# from first_app import views
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.home, name='home'),
    # path('contact/', views.contact, name='contact'),
    # path('about/', views.about, name='about'),
    path('customers/', include('first_app.urls')),

]
