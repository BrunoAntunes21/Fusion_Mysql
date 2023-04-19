from django.urls import path

from .views import IndexView,NotFoundsView,ProccesError
"""a configuração para a rota utilizando uma class 
    based view é por meio de funçoes como está a abaixo """
urlpatterns=[
    path('',IndexView.as_view(),name='index'),
    path('404',NotFoundsView.as_view(),name='404'),
    path('500',ProccesError.as_view(),name='500'),

]