from django.urls import path
from website.views import *

app_name='website'

urlpatterns = [

    path ('',Home_page_view,name='index'),
    path ('category/<str:cat_name>',Home_page_view,name='category'),
    path ('tag/<str:tag_name>',Home_page_view,name='tag'),
    path ('about/',about_view,name='about'),
    path ('contact/',contact_view,name='contact'),
  
]