from django.urls import path
from . import views

app_name = 'test_app'

urlpatterns = [
    path('draw_menu/<str:name>/', views.draw_menu, name='draw_menu'),
]