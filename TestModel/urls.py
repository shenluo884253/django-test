from django.conf.urls import url
from . import views
urlpatterns = [
   url('^zz',views.zz),
   url('add_zz',views.add_zz),
   url('get_anog_list',views.get_anog_list),
   url('get_orgids',views.get_orgids)
]