
from django.contrib import admin
from django.urls import path
import home.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.views.first_page, name='first_page'),
    path('feedback', home.views.feedback, name='feedback'),
    path('contactus', home.views.contactus, name='contactus'),
    path('info', home.views.info, name='info'),
    path('chat', home.views.chat, name='chat'),
]

