from django.contrib import admin
from django.urls import path, include
from .models import Task, Venue, ToDoUser, Event


admin.site.register(Task)
admin.site.register(Venue)
admin.site.register(ToDoUser)
admin.site.register(Event)


# patterns = [
#     path('members/', include('django.contrib.auth.urls')),
#     path('members/', include('members.urls'))
# ]