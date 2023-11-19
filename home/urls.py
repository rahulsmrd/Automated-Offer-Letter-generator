from django.urls import path
from home import views

app_name='home'

urlpatterns = [
    path('',views.index, name='start'),
    path('confirmation/',views.conformation, name='conform'),
    path('preview/<pk>',views.preview, name='preview'),
    path('create', views.create_offerletter, name='create'),
    path('update/<pk>', views.update_offerletter, name='update'),
    path('otp/<pk>', views.otp, name='otp'),
    path('send/<pk>', views.send, name='send')
]