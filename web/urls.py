from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^products/$',views.products, name='products'),
    url(r'^products/(?P<category_id>[0-9]+)/$', views.category, name='category'),
    url(r'^products/(?P<category_id>[0-9]+)/(?P<subcategory_id>[0-9]+)/$', views.subcategory, name='subcategory'),
]