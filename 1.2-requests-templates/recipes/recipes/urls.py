from django.contrib import admin
from django.urls import path

from calculator.views import omlet, pasta, buter, index

urlpatterns = [
    path('', index),
    path('omlet/', omlet),
    path('pasta/', pasta),
    path('buter/', buter),
    path('admin/', admin.site.urls),
]
