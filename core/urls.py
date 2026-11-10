# path: función para definir una ruta individual
from django.urls import path
# views: el archivo de vistas de esta misma app
from . import views

# urlpatterns: lista de rutas que esta app entiende
urlpatterns = [
    # '': la página de inicio que ya tenías
    path('', views.inicio, name='inicio'),
    # nueva ruta 'servicios/' → función views.servicios → alias 'servicios'
    path('servicios/', views.servicios, name='servicios'),
# cierre de la lista urlpatterns
]