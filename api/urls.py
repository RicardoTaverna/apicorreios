from django.contrib import admin
from django.urls import path
from core import views
from teste import views as vw

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home, name='home'),
    path('', views.cliente),
    path('cliente', views.cliente),
    path('show', views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
    path('contato/', vw.contato)
]
