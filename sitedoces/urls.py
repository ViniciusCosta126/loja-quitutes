from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path('produtos', views.produtos, name='produtos'),
    path('sobre', views.sobre, name='sobre'),
    path('contato', views.contato, name='contato'),
    path('produtos/<int:categoria_id>',
         views.produto_categoria, name='produto_categoria')
]
