from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^category/$',views.products, name='products'),
    url(r'^category/(?P<category_id>[0-9]+)/$', views.category, name='category'),
    url(r'^category/(?P<category_id>[0-9]+)/(?P<subcategory_id>[0-9]+)/$', views.subcategory, name='subcategory'),
    url(r'^products/(?P<product_id>[0-9]+)/$', views.product, name='product'),
]