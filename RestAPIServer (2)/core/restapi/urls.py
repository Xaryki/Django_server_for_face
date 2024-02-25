from django.urls  import path
from .views import *

urlpatterns = [
    path('send/photo', SendMessage.as_view())
]