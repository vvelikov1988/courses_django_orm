from django.urls import path     
from . import views
urlpatterns = [
    path('', views.home),
    path('new', views.new),
    path('courses/destroy/<int:course_id>', views.confirm),
    path('courses/destroy/<int:course_id>/confirmed', views.destroy),
]