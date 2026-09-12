from django.urls import path
from . import views

app_name = "app2"
urlpatterns = [
    path('v1_app2/', views.v1_app2, name='vista1_app2'),
    path('v2_app2/', views.v2_app2, name='vista2_app2'),
]