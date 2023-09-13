from django.urls import path
from Blog import views

urlpatterns = [
    path('', views.create_blog, name='create-blog'),
    path('show/', views.show_blogs, name='show-emp'),
]