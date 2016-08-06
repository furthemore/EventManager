from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^cart$', views.getCart, name='cart'),
    url(r'^departments$', views.getDepartments, name='departments'),
    url(r'^pricelevels$', views.getPriceLevels, name='pricelevels'),

]
