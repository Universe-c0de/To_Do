from django.contrib import admin
from django.urls import path, include
from .models import Task


# patterns = [
#     path('members/', include('django.contrib.auth.urls')),
#     path('members/', include('members.urls'))
# ]


admin.site.register(Task)
