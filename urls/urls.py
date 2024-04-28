from django.urls import path
from . import views

urlpatterns=[
    path('add/',views.add,name='Add urls'),
    path('<str:key>',views.redirect,name="Redirect"),
    path('delete/',views.delete,name="Delete"),
    path('get/',views.get,name='get')
]
