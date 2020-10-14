from django.urls import path
from . import views


urlpatterns = [
    path('<int:course_id>/',views.details,name = 'details_page'),
    path('', views.Courses, name='Home-page'),

]
